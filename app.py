# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response, request
import random

api = Flask(__name__)
version = 1.0

@api.route('/information', methods=['GET'])
def getInfo():
    result = {
        'result' : 1,
        'version' : version,
    }

    return make_response(jsonify(result))

@api.route('/tool/signup', methods=['POST'])
def signup():
    payload = request.json
    viewer_id = payload.get('viewer_id')
    user_id = payload.get('user_id')
    name = payload.get('name')

    if viewer_id != None and user_id != None and name != None:
        viewer_id = random.randrange(10000000, 99999999)
        user_id = random.randrange(10000000, 99999999)
        result = {
            'result' : 1,
            'message' : 'ok',
            'viewer_id' : viewer_id,
            'user_id' : user_id
        }
    else:
        result = {
            'result' : 201,
            'message' : ''
        }

    return make_response(jsonify(result))

@api.route('/tool/delete', methods=['POST'])
def delete():
    result = {
        'result' : 202,
        'message' : ''
    }

    return make_response(jsonify(result))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'result' : 404, 'message': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=80)
