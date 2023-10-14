#!/usr/bin/python3

from flask import Blueprint, jsonify

app_views = Blueprint('app_views', __name__)

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "API is up and running"})
