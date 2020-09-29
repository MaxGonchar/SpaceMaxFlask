from http import HTTPStatus


class WrongCredentialsError(Exception):

    def __init__(self):
        super().__init__('Wrong credentials')
        self.message = 'Wrong credentials'
        self.status_code = HTTPStatus.BAD_REQUEST

    def json(self):
        return {
            'status_code': self.status_code,
            'message': self.message
        }
