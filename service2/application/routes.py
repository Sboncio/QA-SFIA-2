from flask import render_template, request
import requests
from random import randint
from application import app
from application.models import weather

@app.route('/gen_random')
def gen_random():
    return randint(1,4)

@app.route('/weather/get', methods=['GET'])
def get_weather():
    #weather = ['Rain','Sun','Snow','Ice']
    num = gen_random()
    weather_result = weather.query.filter_by(id=num).first()
    return weather_result.weathers