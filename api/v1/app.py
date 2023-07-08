#!/usr/bin/python3
"""Main app Module."""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(self):
    """Close down current session."""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Return a JSON-formatted 404 status code response."""
    return (jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    hosts = getenv('HBNB_API_HOST', default='0.0.0.0')
    ports = getenv('HBNB_API_PORT', default=5000)
    app.run(host=hosts, port=ports, threaded=True)
