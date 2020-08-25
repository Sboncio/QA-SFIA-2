from flask import render_template, request, Response
import requests
from random import randint
from application import app
import json

@app.route('/return/data', methods=['GET','POST'])
def returnData():
    data_sent = request.get_json()
    
    if data_sent['speed'] == 'Fast':
        result = 'Slow to appropriate speed'
    elif (data_sent['speed'] == 'Slow' and data_sent['weather'] != 'Sun') or (data_sent['speed'] == 'Average' and data_sent['weather'] == 'Rain'):
        result = 'Proceed with caution'
    elif data_sent['speed'] == 'Average' and (data_sent['weather'] == 'Snow' or data_sent['weather'] == 'Frost'):
        result = 'Slow down'
    elif data_sent['speed'] == 'Average' and data_sent['weather'] == 'Sun':
        result = 'Continue'
    else:
        result = 'Drive with care at appropriate speed'
    return Response(result, mimetype='text/plain')