#!/usr/bin/python3
"""Hello world flask"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/c/<text>')
def c_text(text):
    """c_text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/hbnb')
def hbnb():
    """hbnb"""
    return 'HBNB'


@app.route('/')
def hello_hbnb():
    """hello_hbnb"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
