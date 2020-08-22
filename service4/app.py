from flask import Flask, Response, request
app = Flask(__name__)

@app.route('/return/data', methods=['POST'])
def returnData():
    data_sent = request.get_json()
    return Response("This is the data you sent to the API: " + data_sent['weather'], mimetype='text/plain')

    
if __name__ == '__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')