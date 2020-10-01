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
        link: link to resource.
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
    endpoint: additional path to NASA_API
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


def get_path_to_save(name: str, ext='.jpg') -> str:
    """
    Make path with file name and extension to folder for file needed to save.
    params:
        name: file name
        ext: extension
    return:
        fool path with name in the end
    """
    return os.getcwd() + current_app.config['MEDIA_FOLDER'] + name + ext


def download_file(link: str) -> bytes:
    """
    Download image from link
    params:
        link
    return:
        file in bites
    """
    return requests.get(link).content


def save_file(path: str, data: bytes):
    """
    Save file to folder. If file with same name exists, it will be rewritten
    params:
        path: fool path with name in the end
        data: file in bites
    """
    with open(path, 'wb') as file:
        file.write(data)


def jsonify_data():
    pass


def jsonify_error():
    pass
