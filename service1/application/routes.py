from flask import render_template, request

from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#@app.route('/weather')
#def getWeather():
    #response = requests.get('http://service2:5001/weather/get')
