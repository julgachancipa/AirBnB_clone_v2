#!/usr/bin/python3
"""Hello world flask"""
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/number_template/<int:n>')
def num_template(n):
    """hbnb"""
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>')
def only_int(n):
    """hbnb"""
    return '%d is a number' % n


@app.route('/python/')
@app.route('/python/<text>/')
def py_text(text='is cool'):
    """hbnb"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/c/<text>')
def c_text(text):
    """hbnb"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/hbnb')
def hbnb():
    """hbnb"""
    return 'HBNB'


@app.route('/')
def hello_hbnb():
    """hbnb"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
