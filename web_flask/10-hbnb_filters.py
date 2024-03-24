#!/usr/bin/python3
"""
Starts a Flask web application with filters.
"""
from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display the HBNB filters HTML page."""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
