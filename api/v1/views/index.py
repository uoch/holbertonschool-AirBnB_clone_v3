#!/usr/bin/python3
"""
mport app_views from api.v1.views
create a route /status on the object
app_views that returns a JSON: "status" ok
"""
from . import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    return jsonify({"status": "OK"})
