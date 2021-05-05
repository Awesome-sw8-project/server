from flask import Flask, request
import estimator.estimate as est
import jreq_parser.req_parser as parser
import json

app = Flask(__name__)

# Entry point.
@app.route('/', methods = ['POST'])
def entry():
    try:
        data = parser.parse_json(json.dumps(request.get_json()))
        estimated_position = None

        for element in data:
            estimated_position = est.estimate(element)

        return json.dumps({"x": estimated_position[0], "y": estimated_position[1], "z": estimated_position[2]})
    
    except Exception as exc:
        return "JSON parse error."

# Error point.
@app.route('/', methods = ['GET'])
def error():
    return "This should have been a POST request."

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 52200)