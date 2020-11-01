import os
from http import HTTPStatus

import requests
from authlib.jose import jwt
from authlib.jose.errors import BadSignatureError, DecodeError
from flask import current_app, request

from api.errors import (
    RequestDataError,
    AuthorizationError
)


def get_nasa_data(url: str, params: dict) -> dict:
    """
    Get data from NASA endpoint.
    params:
        url: endpoint;
        params: params for request
    return:
        dict with data if it had been provided, else - NO_DATA message.
    """
    no_data = {'Sorry': 'There are no data for the specified period.'}

    response = requests.get(url, params=params)

    if response.status_code == HTTPStatus.FORBIDDEN:
        raise AuthorizationError('Wrong NASA API key')

    response.raise_for_status()

    if response.text:
        res = response.json()
    else:
        res = no_data
    return res


def url_for(endpoint: str) -> str:
    """
    Make URL for NASA endpoint
    endpoint: additional path to NASA_API
    """
    return current_app.config.get('NASA_API').format(endpoint=endpoint)


def get_jwt_token() -> [str, Exception]:
    """
    Parse incoming request's header to type and jwt token and validate them.
    return:
        jwt token if validation is passed
    """
    expected_errors = {
        KeyError: 'Authorization header is missed',
        AssertionError: 'Wrong authorization type',
        ValueError: 'Incorrect jwt entering'
    }
    try:
        scheme, token = request.headers['Authorization'].split()
        assert scheme.lower() == 'bearer'
        return token
    except tuple(expected_errors) as error:
        raise AuthorizationError(expected_errors[error.__class__])


def get_auth_token() -> [str, Exception]:
    """
    Validate and decode jwt to get authorization token.
    return:
        authorization token if validation is passed.
    """
    expected_errors = {
        KeyError: 'Wrong JWT payload structure',
        TypeError: '<SECRET_KEY> is missing',
        DecodeError: 'Wrong JWT structure',
        BadSignatureError: 'Failed to decode JWT with provided key'
    }
    token = get_jwt_token()
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'])
        return payload['key']
    except tuple(expected_errors) as error:
        raise AuthorizationError(expected_errors[error.__class__])


def get_json(schema) -> [dict, Exception]:
    """
    Get data from request's body,
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


def get_params(schema) -> [dict, Exception]:
    """
    Get data from request's url,
    validate, using marshmallow's schema and return it in dict
    params:
        schema: marshmallow's schema for validation
    return:
        data in dict
    """
    data = dict(request.args)
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
    return os.path.join(
        os.getcwd(),
        current_app.config['MEDIA_FOLDER'],
        name + ext
    )


def download_file(link: str) -> bytes:
    """
    Download image from link
    params:
        link
    return:
        file in bites
    """
    return requests.get(link).content


def save_file(path: str, data: bytes) -> None:
    """
    Save file to folder. If file with same name exists, it will be rewritten
    params:
        path: fool path with name in the end
        data: file in bites
    """
    with open(path, 'wb') as file:
        file.write(data)
