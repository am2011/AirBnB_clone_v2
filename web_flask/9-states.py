#!/usr/bin/python3
"""Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>."""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """all State"""
    states = storage.all("State")
    if len(storage.all("State")) == 0:
        states = 0
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """ render the id if exist """
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def remove_session(exception):
    """removing the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")