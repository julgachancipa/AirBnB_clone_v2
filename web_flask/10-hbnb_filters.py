#!/usr/bin/python3
"""List of states"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_s(x=None):
    """close session at the end"""
    storage.close()


@app.route('/hbnb_filters')
def filters():
    """display hbnb page"""
    states_id_nm = []
    all_states = storage.all('State')

    for i in all_states:
        states_id_nm.append((all_states[i].id, all_states[i].name))
    states = sorted(states_id_nm, key=lambda x: x[1])

    cities_id_nm = []
    all_cities = storage.all('City')
    for i in all_cities:
        cities_id_nm.append((all_cities[i].id, all_cities[i].name,
                             all_cities[i].state_id))
    cities = sorted(cities_id_nm, key=lambda x: x[1])

    amenities = []
    all_amenities = storage.all('Amenity')
    for k, am in all_amenities.items():
        amenities.append(am.name)
    amenities.sort()

    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
