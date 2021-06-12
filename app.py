# Basic flask imports
from flask import Flask, request, json
from dotenv import load_dotenv
from stock_queries import StockAPI
from stocks import *

load_dotenv()
app = Flask(__name__)
DEBUG=True



@app.route('/')
def index():
    return 'Working!'

@app.route('/daily')
def daily():
    data = StockAPI.get_all_screeners()
    return json.jsonify(data)

if __name__ == '__main__':
    app.run(debug=DEBUG)