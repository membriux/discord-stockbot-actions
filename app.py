# Basic flask imports
from flask import Flask, request, json
import os

app = Flask(__name__)
DEBUG=True


@app.route('/')
def index():
    result = {'hello': 'hello'}
    return json.jsonify()






if __name__ == '__main__':
    app.run(debug=DEBUG)