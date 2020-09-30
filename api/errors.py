from http import HTTPStatus


class SMFError(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def json(self):
        return {
            'status_code': self.status_code,
            'message': self.message
        }


class WrongCredentialsError(SMFError):

    def __init__(self):
        super().__init__('Wrong credentials', HTTPStatus.BAD_REQUEST)
