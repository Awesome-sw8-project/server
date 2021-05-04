from flask import Flask, request
import estimator.estimate as est
import jreq_parser.req_parser

app = Flask(__name__)

# Entry point.
@app.route('/')
def entry():
     return est.estimate()

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 52200)
