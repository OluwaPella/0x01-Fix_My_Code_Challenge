#!/usr/bin/python3
""" Index view
"""
from flask import Blueprint, jsonify

from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ 
    Status of the web server

    """
    return jsonify({"status": "OK"})
