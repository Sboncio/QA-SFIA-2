from unittest.mock import patch
from flask import url_for, jsonify
from flask_testing import TestCase
from application import app
import json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_response(self):
        with patch('flask.request.get_json')as g:
            g['weather']= 'Sun'
            g['speed']='Average'

            #g.return_value.data = jsonify({'weather':'Sun', 'speed':'Average'})

            response = self.client.get(url_for('returnData'))
            self.assertIn(b'Continue',response.data)
