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


@app.route('/states_list')
def states_l():
    """display HTML page"""
    states_id_nm = []

    all_states = storage.all('State')

    for i in all_states:
        states_id_nm.append((all_states[i].id, all_states[i].name))

    states = sorted(states_id_nm, key=lambda x: x[1])
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
