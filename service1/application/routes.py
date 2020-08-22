from flask import render_template, request
import requests
from application import app

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

@app.route('/send_data', methods=['POST'])
def sendData(weather, speed):
    response = requests.post('http://service4:5003/return/data', json={'weather': weather, 'speed': speed})
    return response.text

@app.route('/communicate')
def communicate():
    weather = getWeather()
    speed = getSpeed()
    result = sendData(weather, speed)
    return render_template('results.html', weather=weather,speed=speed,result=result)
