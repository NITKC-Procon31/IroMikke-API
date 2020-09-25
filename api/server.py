from flask import Flask, request
from .endpoint import Information, SignUp
from .handler import Handler

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
    return handler.handle_signup(request.json, request.headers)

@app.errorhandler(404)
def not_found(error):
    return handler.handle_404()
