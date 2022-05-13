import flask
from flask import Flask, request
from flask_ngrok import run_with_ngrok
# from flask.ext.cors import CORS, cross_origin
app = Flask(__name__)
run_with_ngrok(app)


@app.route('/istimeframe')
def hello():
    args = request.args
    print(args)
    arrivaldate = args.get('arrival')
    departuredate = args.get('departure')
    response = flask.jsonify(mockDatabase(arrivaldate,departuredate))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def mockDatabase(arrival,departure):
    print(arrival,departure)
    mockdates = ['2022-05-14','2022-05-16','2022-05-18','2022-05-22','2022-05-24','2022-05-27']
 
    if arrival in mockdates or departure in mockdates:
        return {'status':False, 'msg':"Date timeframe is not available"}

    else:
        return {'status':True, 'msg':"Date timeframe is available"}

if __name__ == "__main__":
    app.run()

