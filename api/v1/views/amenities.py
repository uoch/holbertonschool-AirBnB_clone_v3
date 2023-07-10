#!/usr/bin/python3
"""
Create a new view for Amenity objects that
handles all default RESTFul API actions:
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'],
                 strict_slashes=False)
def Amenity1():
    slist = []
    states = storage.all(Amenity).values()
    for state in states:
        slist.append(state.to_dict())
    return jsonify(slist)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def Amenity2(amenity_id):
    """Retrieves a State object"""
    states = storage.all(Amenity)
    key = "Amenity."+amenity_id
    if key not in states:
        abort(404)
    a = states[key]
    return jsonify(a.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def Amenity3(amenity_id):
    states = storage.all(Amenity)
    key = "Amenity."+amenity_id
    if key not in states:
        abort(404)
    a = states[key]
    storage.delete(a)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'],
                 strict_slashes=False)
def pAmenity4():
    js = request.get_json()
    if not js:
        abort(400, 'Not a JSON')
    if 'name' not in js:
        abort(400, 'Missing name')
    state = Amenity(**js)
    storage.new(state)
    storage.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    all_amenities = storage.all(Amenity)
    amenity_key = "Amenity." + amenity_id
    if amenity_key not in all_amenities:
        abort(404)
    request_data = request.get_json()
    if not request_data:
        abort(400, 'Not a JSON')
    amenity = all_amenities[amenity_key]
    for key, value in request_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
