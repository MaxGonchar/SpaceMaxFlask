import requests
import os
from authlib.jose import jwt
from flask import current_app, request

from api.errors import WrongCredentialsError, RequestDataError


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

    # not in all day's json 'hdurl' exists
    link = res['hdurl'] if params['hd'] and res.get('hdurl') else res['url']

    return {
        'explanation': res['explanation'],
        'link': link
    }


def url_for(endpoint: str) -> str:
    """
    Make URL for NASA endpoint
    path: additional path to NASA_API
    """
    return current_app.config.get('NASA_API').format(endpoint=endpoint)


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


def get_json(schema) -> dict:
    """
    Get data from request,
    validate, using marshmallow's schema and return it in dict
    params:
        schema: marshmallow's schema for validation
    return:
        data in dict
    """
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        raise RequestDataError('\n'.join(sum(errors.values(), [])))
    return data


def download_image(link: str, name: str):
    """
    Download image to MEDIA_FOLDER.
    If file with same name exists, it will be rewritten.
    """
    path = os.getcwd() + current_app.config['MEDIA_FOLDER'] + name + '.jpg'
    with open(path, 'wb') as file:
        file.write(requests.get(link).content)


def jsonify_data():
    pass


def jsonify_error():
    pass
