#!/usr/bin/python3
"""TODO: DOC"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
