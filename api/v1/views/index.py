#!/usr/bin/python3
"""Index endpoint."""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def status():
    """Return status in JSON."""
    return jsonify(status="OK")


@app_views.route('/stats')
def stat():
    """Endpoint that retrieves the number of objs by type."""
    classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    counter = {}
    for cls in classes:
        counter[cls] = storage.count(classes[cls])
    return jsonify(counter)