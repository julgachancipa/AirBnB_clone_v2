#!/usr/bin/python3
"""List of states"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_s(x=None):
    """colse session at the end"""
    storage.close()


@app.route('/states/<id>')
def cities_st_l(id):
    """display HTML page"""

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
    name = None
    for st in states:
        if(st[0] == id):
            name = st[1]

    print('>>>', name)
    return render_template('9-states.html', states=states,
                           filt_state=id, cities=cities,
                           name=name)


@app.route('/states')
def states_l():
    """display HTML page"""
    states_id_nm = []

    all_states = storage.all('State')

    for i in all_states:
        states_id_nm.append((all_states[i].id, all_states[i].name))

    states = sorted(states_id_nm, key=lambda x: x[1])
    return render_template('9-states.html', states=states,
                           filt_state=None, cities=None,
                           name=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
