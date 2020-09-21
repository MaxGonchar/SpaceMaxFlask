from authlib.jose import jwt

from config import SECRET_KEY


def get_payload(token):
    """Decode data form jwt"""
    return dict(jwt.decode(token, SECRET_KEY))


