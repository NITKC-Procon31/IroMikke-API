import api.server
from .data_headers import DataHeaders
from .result_code import ResultCode
from .endpoint import Information, SignUp
from .cryptographer import Cryptographer
from .models.user import User
from .user_manager import UserManager
from flask import jsonify, make_response, abort

class Handler:
    def handle_information(self):
        endpoint: Information = Information(api.server.VERSION)
        return self.success(
            DataHeaders.dummy(ResultCode.RC_SUCCESS),
            endpoint.response()
        )

    def handle_signup(self, request: dict, headers):
        data_headers: DataHeaders = self.get_data_headers(headers)
        endpoint: SignUp = SignUp.request(request)
        if endpoint is None:
            return self.error(ResultCode.RC_SIGNUP_ERROR, 'The field is invalied.')
        else:
            user: User = UserManager.generate(endpoint.name)

            return self.success(
                DataHeaders(user.viewer_id, user.user_id).to_dict(ResultCode.RC_SUCCESS),
                endpoint.response()
            )

    def handle_404(self):
        return make_response(jsonify({'result' : 404, 'message': 'Not found'}), 404, {"Content-Type": "application/json"})

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

    def get_data_headers(self, headers):
        if not headers.has_key('USER-ID'):
            abort(403)

        try:
            id: str = Cryptographer.decode(headers.get('USER-ID'))
            viewer_id, user_id = map((lambda x: int(x)), id.split('+'))
            if not (100000000 <= viewer_id <= 999999999 and 100000000 <= user_id <= 999999999):
                abort(403)

            return DataHeaders(viewer_id=viewer_id, user_id=user_id)
        except:
            abort(403)
