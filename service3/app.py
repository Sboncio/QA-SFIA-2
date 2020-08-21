from flask import Flask, Response, request
from random import randint
app = Flask(__name__)

speeds = ['Slow', 'Average', 'Fast']

@app.route('/speed/get', methods=['GET'])
def get_weather():
    return Response(speeds[randint(0,2)], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')