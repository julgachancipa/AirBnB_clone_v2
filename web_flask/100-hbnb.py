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


@app.route('/hbnb')
def filters():
    """display hbnb page"""

    """States list"""
    states_id_nm = []
    all_states = storage.all('State')

    for i in all_states:
        states_id_nm.append((all_states[i].id, all_states[i].name))
    states = sorted(states_id_nm, key=lambda x: x[1])

    """Cities list"""
    cities_id_nm = []
    all_cities = storage.all('City')
    for i in all_cities:
        cities_id_nm.append((all_cities[i].id, all_cities[i].name,
                             all_cities[i].state_id))
    cities = sorted(cities_id_nm, key=lambda x: x[1])

    """Amenities list"""
    amenities = []
    all_amenities = storage.all('Amenity')
    for k, am in all_amenities.items():
        amenities.append(am.name)
    amenities.sort()

    """Places list"""
    places_info = []
    all_places = storage.all('Place')
    for i in all_places:
        places_info.append((all_places[i].name, all_places[i].price_by_night,
                            all_places[i].max_guest, all_places[i].number_rooms,
                            all_places[i].number_bathrooms,
                            all_places[i].user.first_name,
                            all_places[i].description
        ))
    places = sorted(places_info, key=lambda x: x[0])
    return render_template('100-hbnb.html', states=states,
                           cities=cities, amenities=amenities,
                           places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
