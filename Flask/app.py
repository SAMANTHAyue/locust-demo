#!/usr/bin/env python
from flask import jsonify
from datetime import datetime
from flask import Flask
from google.appengine.ext import vendor
vendor.add('lib')


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/datetime')
def get_datetime():
    data = {'datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
