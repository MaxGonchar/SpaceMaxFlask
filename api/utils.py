import requests
from authlib.jose import jwt
from flask import current_app, request

from api.errors import WrongCredentialsError


def get_apod(url: str, params: dict) -> dict:
    """
    Return link to picture of the day and picture's description.

    params:
        url: NASA "APOD"-api's endpoint;
        params: for request
            api_key: NASA token;
            date: date for day's picture;
            hd: True - high definition, False - lowe definition;

    return - dict, where
        explanation: picture's description
        link: link for downloading.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    res = response.json()

    link = res['hdurl'] if params['hd'] == 'True' else res['url']

    return {
        'explanation': res['explanation'],
        'link': link
    }


def url_for(path: str) -> str:
    """
    Make URL for NASA endpoint
    path: additional path to NASA_API
    """
    return current_app.config.get('NASA_API').format(path=path)


def get_jwt():
    """
    Validate credentials and decode NASA api_key from jwt
    """
    try:
        scheme, token = request.headers['Authorization'].split()
        assert scheme.lower() == 'bearer'
    except (KeyError, ValueError, AssertionError):
        raise WrongCredentialsError

    return jwt.decode(token, current_app.config['SECRET_KEY'])['key']


def get_json() -> dict:
    pass


def download_image(link: str, path: str):
    pass


def jsonify_data():
    pass


def jsonify_error():
    pass
