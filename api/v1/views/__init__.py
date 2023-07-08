#!/usr/bin/python3
"""Initializer."""
from flask import Blueprint
from api.v1.views.states import *

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")