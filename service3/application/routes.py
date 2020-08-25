from flask import render_template, request
import requests
from random import randint
from application import app

@app.route('/gen_random')
def gen_random():
    return randint(0,2)

@app.route('/speed/get', methods=['GET'])
def get_speeds():
    speeds = ['Slow', 'Average', 'Fast']
    num=gen_random()
    result = speeds[num]
    return result