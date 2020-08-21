from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/return/data', methods=['POST'])
def returnData():
    data_sent = request.data.decode('utf-8')
    upper_data = data_sent.upper()
    return Response("This is the data you sent to the API but in upper case: " + upper_data, mimetype='text/plain')

    
if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')