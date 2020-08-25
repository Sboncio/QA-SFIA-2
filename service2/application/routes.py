from flask import render_template, request
import requests
from random import randint
from application import app

@app.route('/gen_random')
def gen_random():
    return randint(0,3)

@app.route('/weather/get', methods=['GET'])
def get_weather():
    weather = ['Rain','Sun','Snow','Ice']
    num = gen_random()
    result = weather[num]
    return result

