from flask import render_template, request
import requests
from application import app, db
from application.models import results

weather_data = ''
speed_data = ''

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/weather')
def getWeather():
    response = requests.get('http://service2:5001/weather/get')
    return response.text

@app.route('/speed')
def getSpeed():
    response = requests.get('http://service3:5002/speed/get')
    return response.text

@app.route('/send_data/<weather_data>/<speed_data>', methods=['GET','POST'])
def sendData(weather_data, speed_data):
    response = requests.post('http://service4:5003/return/data', json={'weather': weather_data, 'speed': speed_data})
    return response.text

@app.route('/communicate', methods=['GET','POST'])
def communicate():
    weather_data = getWeather()
    speed_data = getSpeed()
    result_data = sendData(weather_data,speed_data)
    result_post = results(weather=weather_data,speed=speed_data,result=result_data)
    #db.session.add(result_post)
    #db.session.commit()
    return render_template('results.html', weather=weather_data,speed=speed_data,result=result_data)