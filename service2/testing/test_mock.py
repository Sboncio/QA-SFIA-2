from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app
from time import sleep

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_random_weather(self):
        sleep(10)
        with patch('application.routes.gen_random') as g:
            g.return_value.data = 0

            response = self.client.get(url_for('get_weather'))
            self.assertIn(b'Sun', response.data)

    def test_random_num(self):
        with patch('random.randint') as g:
            g.return_value.data = str(1)
            response = self.client.get(url_for('gen_random'))
            self.assertIn(b'1', response.data)