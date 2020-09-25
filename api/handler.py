import api.server
from .data_headers import DataHeaders
from .result_code import ResultCode
from .endpoint import Information, SignUp
from flask import jsonify, make_response

class Handler:
    def handle_information(self):
        endpoint: Information = Information(api.server.VERSION)
        return self.success(
            DataHeaders.dummy(ResultCode.RC_SUCCESS),
            endpoint.response()
        )

    def handle_signup(self, request: dict):
        endpoint: SignUp = SignUp.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_SIGNUP_ERROR, 'The field is invalied.')
        else:
            pass

    def handle_404(self):
        return make_response(jsonify({'result' : 404, 'message': 'Not found'}), 404)

    def success(self, data_headers: dict, data: dict):
        return self.response({
            'data_headers': data_headers,
            'data': data
        }, 200)

    def error(self, result_code: int, message: str):
        return self.response({
            'data_headers': DataHeaders.dummy(result_code),
            'data': {
                'message': message
            }
        }, 400)

    def response(self, data: dict, http_status: int):
        return make_response(jsonify(data), http_status, {"Content-Type": "application/json"})
