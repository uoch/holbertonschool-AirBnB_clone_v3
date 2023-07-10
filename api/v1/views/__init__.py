#!/usr/bin/python3
"""
views inside v1
"""

from flask import Blueprint

# Create the app_views Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the views module after creating the app_views Blueprint
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
