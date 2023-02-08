#!/usr/bin/python3
""" a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Hello HBNB! String on main Route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ Display a message """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': "is_cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """The default value of text is “is cool” """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ display “n is a number” only if n is an integer"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """ display “n is a number” only if n is an integer"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """ display “n is a number” only if n is an integer with an if conditon """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
