from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_speed_fast(self):
        with patch('requests.get')as g:
            g.return_value.text = 'Slow'
            response = self.client.get(url_for('getSpeed'))

            self.assertIn(b'Slow', response.data)

    def test_weather_snow(self):
        with patch('requests.get')as g:
            g.return_value.text = 'Frost'
            response = self.client.get(url_for('getWeather'))

            self.assertIn(b'Frost', response.data)

    def test_send_data(self):
        with patch('requests.post')as g:
            g.return_value.text = 'Continue'
            response = self.client.get(url_for('sendData',weather_data='Sun',speed_data='Average'))

            self.assertIn(b'Continue', response.data)

    def test_home_get(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_communicate(self):
        with patch('application.routes.getWeather') as g, patch('application.routes.getSpeed') as h, patch('application.routes.sendData') as i:
            g.return_value.text = 'Sun'
            h.return_value.text = 'Average'
            i.return_value.text = 'Continue'

            response = self.client.get(url_for('communicate'))
            self.assertEqual(response.status_code,200)