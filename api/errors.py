from http import HTTPStatus


AUTH_ERROR = 'authorization error'


class SMFError(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

    def json(self):
        return {
            'code': self.code,
            'message': self.message
        }


class RequestDataError(SMFError):

    def __init__(self, message):
        super().__init__(message, code=HTTPStatus.BAD_REQUEST)


class AuthorizationError(SMFError):

    def __init__(self, message):
        super().__init__(message, AUTH_ERROR)
