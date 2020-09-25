from flask import request, current_app

from authlib.jose import jwt
from authlib.jose.errors import JoseError


def json_valid():
    pass


def jwt_valid() -> dict:
    """
    Checking user's credentials
    return:
        Ok: decoded credentials
        Not ok: empty dict
    """
    try:
        scheme, token = request.headers['Authorization'].split()
        assert scheme.lower() == 'bearer'
        return jwt.decode(token, current_app.config['SECRET_KEY'])
    except (KeyError, ValueError, AssertionError, JoseError):
        return {}
