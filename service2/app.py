from flask import Flask, Response, request
from random import randint
app = Flask(__name__)

weather = ['Rain','Sun','Snow','Ice']

@app.route('/weather/get', methods=['GET'])
def get_weather():
    return Response(weather[randint(0,3)], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')