import api.server
from api.data_headers import DataHeaders
from api.exception import InvaliedTypeException

class Get:
    def response(self):
        pass

    @classmethod
    def http_method(cls):
        return ['GET']

class Post(Get):
    @classmethod
    def request(cls, dic: dict):
        pass

    @classmethod
    def http_method(cls):
        return ['POST']

class Information(Get):
    version: float

    def __init__(self, version):
        self.version = version

    def response(self):
        return {
            'version': self.version
        }


class SignUp(Post):
    name: str
    viewer_id: int
    user_id: int

    def __init__(self, name: str, viewer_id: int, user_id: int):
        self.name = name
        self.viewer_id = viewer_id
        self.user_id = user_id

    def response(self):
        return []

    @classmethod
    def request(cls, dic: dict):
        try:
            return SignUp(name=Validator.validate_str(dic['name']),
                          viewer_id=Validator.validate_int(dic['viewer_id']),
                          user_id=Validator.validate_int(dic['user_id']))
        except KeyError:
            return None
        except InvaliedTypeException:
            return None

class GetProfile(Post):
    name: str
    viewer_id: int

    def __init__(self, viewer_id: int):
        self.viewer_id = viewer_id

    def response(self):
        return {
            'name': self.name,
            'viewer_id': self.viewer_id
        }

    @classmethod
    def request(cls, dic: dict):
        try:
            return GetProfile(viewer_id=Validator.validate_int(dic['viewer_id']))
        except KeyError:
            return None
        except InvaliedTypeException:
            return None


class Validator:
    @classmethod
    def validate_int(cls, i: int):
        if type(i) == int:
            return i
        else:
            raise InvaliedTypeException('%s is not int' % type(i))

    @classmethod
    def validate_str(cls, s: str):
        if type(s) == str:
            return s
        else:
            raise InvaliedTypeException('%s is not str' % type(s))

    @classmethod
    def validate_float(cls, f: float):
        if type(f) == float:
            return f
        else:
            raise InvaliedTypeException('%s is not float' % type(f))

    @classmethod
    def validate_list(cls, l: list):
        if type(l) == list:
            return l
        else:
            raise InvaliedTypeException('%s is not list' % type(l))

    @classmethod
    def validate_dict(cls, d: dict):
        if type(d) == dict:
            return d
        else:
            raise InvaliedTypeException('%s is not dict' % type(d))

    @classmethod
    def validate_bool(cls, b: bool):
        if type(b) == bool:
            return b
        else:
            raise InvaliedTypeException('%s is not bool' % type(b))
