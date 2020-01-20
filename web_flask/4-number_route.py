#!/usr/bin/python3
"""Hello world flask"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/number/<int:n>')
def only_int(n):
    return '%d is a number' % n

@app.route('/python/')
@app.route('/python/<text>/')
def py_text(text='is cool'):
    return 'Python %s' % text.replace('_', ' ')


@app.route('/c/<text>')
def c_text(text):
    return 'C %s' % text.replace('_', ' ')

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
