from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/return/data', methods=['POST'])
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

    
if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')