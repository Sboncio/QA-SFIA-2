from unittest.mock import patch
from flask import url_for, jsonify
from flask_testing import TestCase
from application import app
import json

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_response_fast(self):
        
        response = self.client.post(url_for('returnData'), json = {'weather':'Sun','speed':'Fast'})
        self.assertIn(b'Slow to appropriate speed',response.data)

    def test_response_caution(self):
        
        response = self.client.post(url_for('returnData'), json = {'weather':'Rain','speed':'Average'})
        self.assertIn(b'Proceed with caution',response.data)

    def test_response_slow_down(self):
        
        response = self.client.post(url_for('returnData'), json = {'weather':'Snow','speed':'Average'})
        self.assertIn(b'Slow down',response.data)

    def test_response_continue(self):
        
        response = self.client.post(url_for('returnData'), json = {'weather':'Sun','speed':'Average'})
        self.assertIn(b'Continue',response.data)

    def test_response_drive(self):
        
        response = self.client.post(url_for('returnData'), json = {'weather':'Sun','speed':'Slow'})
        self.assertIn(b'Drive with care at appropriate speed',response.data)
