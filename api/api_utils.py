from flask import current_app
from authlib.jose import jwt


def get_payload(token):
    """Decode data form jwt"""
    print(current_app.config.get('SECRET_KEY'))
    return dict(jwt.decode(token, current_app.config.get('SECRET_KEY')))


