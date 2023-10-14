#!/usr/bin/python3

# Web server

from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=5000,  debug=True)
