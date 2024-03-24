#!/usr/bin/python3
"""
Starts a Flask web application that
displays a list of states and their cities.
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all states."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states, state_id=None)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a HTML page with a list of cities for a specific state."""
    states = storage.all(State).values()
    state = next((state for state in states if state.id == id), None)
    return render_template('9-states.html', states=states,
                           state_id=id, state=state)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
