#!/usr/bin/python3
"""
Create a new view for State objects that handles
all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.state import State
import models


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def status():
    states = storage.all(State).values()
    list_state = [state.to_dict() for state in states]
    return jsonify(list_state)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object"""
    states = storage.all(State)
    key = f"State.{state_id}"
    state = states.get(key)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    key = f"State.{state_id}"
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post():
    """Creates a new State object"""
    js = request.get_json()
    if not js or 'name' not in js:
        abort(400, 'Invalid JSON or missing name')

    state = State(**js)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put(state_id):
    """Updates a State object"""
    js = request.get_json()
    key = f"State.{state_id}"
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not js:
        abort(400, 'Not a JSON')
    for attr, value in js.items():
        if attr not in ["id", "created_at", "updated_at"]:
            setattr(state, attr, value)
    storage.save()
    return jsonify(state.to_dict()), 200
