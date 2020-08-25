from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_random_speed(self):
        with patch('application.routes.gen_random') as g:
            g.return_value.data = 2

            response = self.client.get(url_for('get_speeds'))
            self.assertIn(b'Average', response.data)

    def test_random_num(self):
        with patch('random.randint') as g:
            g.return_value.data = str(0)
            response = self.client.get(url_for('gen_random'))
            self.assertIn(b'0', response.data)