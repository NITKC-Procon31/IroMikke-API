# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request
from .endpoint import Information, SignUp, UpdateUserName
from .handler import Handler
import random, time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False
handler = Handler()
VERSION = 1.0

def run(host, port):
    app.run(host=host, port=port)

@app.route('/information', methods=Information.http_method())
def getInfo():
    return handler.handle_information()

@app.route('/tool/signup', methods=SignUp.http_method())
def signup():
    return handler.handle_signup(request.json)

@app.route('/user/update_name', methods=UpdateUserName.http_method())
def update_user_name():
    pass

@app.errorhandler(404)
def not_found(error):
    return handler.handle_404()
