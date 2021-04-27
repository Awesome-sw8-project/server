from flask import Flask, request

app = Flask(__name__)

# Entry point.
@app.route('/')
def entry():
     return "Hello, dude!"

if (__name__ == "__main__"):
    app.run(host = '0.0.0.0', port = 52200)