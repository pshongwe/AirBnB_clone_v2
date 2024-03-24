#!/usr/bin/python3
from flask import Flask, render_template
from models import storage, State, City, Amenity, Place

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    places = storage.all(Place).values()
    places = sorted(places, key=lambda place: place.name)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

