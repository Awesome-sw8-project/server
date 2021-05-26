from flask import Flask, request, make_response
import estimator.estimate as est
import estimator.experiments.hybrid as hbrd
import jreq_parser.req_parser as parser
import json

app = Flask(__name__)

# Entry point.
@app.route('/', methods = ['POST'])
def entry():
    try:
        data = parser.parse_json(json.dumps(request.get_json()))

        if len(data) == 0:
            return make_response("No input measurements given.", 406)

        estimated_position = None
        hybrid = hbrd.PDRMLHybrid(data[0].get_start_location(), "lightgbm")

        for element in data:
            estimated_position = est.estimate(hybrid, element)

        return json.dumps({"x": estimated_position[0], "y": estimated_position[1], "z": estimated_position[2]})

    except Exception as exc:
        return make_response("JSON parse error.", 406)

# Error point.
@app.route('/', methods = ['GET'])
def error():
    return "This should have been a POST request."

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 52200)
