from flask import render_template, request
import requests
from random import randint
from application import app
from application.models import speed

@app.route('/gen_random')
def gen_random():
    return randint(1,3)

@app.route('/speed/get', methods=['GET'])
def get_speeds():
    #speeds = ['Slow', 'Average', 'Fast']
    num=gen_random()
    #result = speeds[num]
    speed_result = speed.query.filter_by(id=num).first()
    return speed_result.speeds