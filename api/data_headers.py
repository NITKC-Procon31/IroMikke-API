import time

class DataHeaders:
    def __init__(self, viewer_id: int, user_id: int):
        self.__viewer_id = viewer_id
        self.__user_id = user_id

    @property
    def viewer_id(self):
        return self.__viewer_id

    @property
    def user_id(self):
        return self.__user_id

    @viewer_id.setter
    def viewer_id(self, viewer_id: int):
        self.__viewer_id = viewer_id

    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    def to_dict(self, result_code: int):
        return {
            'viewer_id': self.viewer_id,
            'user_id': self.user_id,
            'timestamp': int(time.time()),
            'result_code': result_code
        }

    @classmethod
    def dummy(cls, result_code: int):
        return DataHeaders(0, 0).to_dict(result_code)

