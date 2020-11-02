from http import HTTPStatus
from unittest.mock import patch, Mock

from authlib.jose import jwt
from requests import Session
from pytest import fixture

from api.errors import AUTH_ERROR
from app import app
from .method_strategy import Method, Post, Get
from .utils import get_header


def routes():
    yield '/api/dayimage'
    yield '/api/cme'


def make_request(client, route, headers, json, params):
    methods = {
        'dayimage': Method(Post()),
        'cme': Method(Get())
    }
    return methods[route.split('/')[-1]].get_response(
        client, route, headers, json, params
    )


@fixture(scope='module', params=routes(), ids=lambda route: route)
def route(request):
    return request.param


@fixture(scope='module')
def jwt_with_wrong_payload_structure():
    header = {'alg': 'HS256'}
    payload = {'not_key': 'some_key'}
    key = app.secret_key
    return jwt.encode(header, payload, key).decode('ascii')


@fixture(scope='module')
def jwt_encoded_by_wrong_key():
    header = {'alg': 'HS256'}
    payload = {'not_key': 'some_key'}
    key = 'wrong_key'
    return jwt.encode(header, payload, key).decode('ascii')


def authorization_errors_expected_payload(message):
    return {
        'code': AUTH_ERROR,
        'message': f'{message}'
    }


def test_call_with_no_authorization_header(
        route, client, valid_jwt, valid_json, valid_params
):
    response = make_request(client, route, get_header(valid_jwt, header=''),
                            valid_json, valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Authorization header is missed'
    )


def test_call_with_wrong_authorization_type(
        route, client, valid_jwt, valid_json, valid_params
):
    response = make_request(client, route,
                            get_header(valid_jwt, auth_type='NotBearer'),
                            valid_json, valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Wrong authorization type'
    )


def test_call_with_incorrect_jwt_entering(
        route, client, valid_json, valid_params
):
    response = make_request(client, route, get_header(' '), valid_json,
                            valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Incorrect jwt entering'
    )


def test_call_with_wrong_jwt_structure(
        route, client, valid_json, valid_params
):
    response = make_request(client, route,
                            get_header('jwt_with_wrong_structure'),
                            valid_json, valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Wrong JWT structure'
    )


def test_call_with_wrong_jwt_payload_structure(
        route, client, valid_json, jwt_with_wrong_payload_structure,
        valid_params
):
    response = make_request(client, route,
                            get_header(jwt_with_wrong_payload_structure),
                            valid_json, valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Wrong JWT payload structure'
    )


def test_call_with_jwt_encoded_wrong_key(
        route, client, valid_json, jwt_encoded_by_wrong_key, valid_params
):
    response = make_request(client, route,
                            get_header(jwt_encoded_by_wrong_key),
                            valid_json, valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Failed to decode JWT with provided key'
    )


def test_call_with_no_secret_key(
        route, client, valid_json, valid_jwt, valid_params
):
    key = app.secret_key
    app.secret_key = None
    response = make_request(client, route, get_header(valid_jwt),
                            valid_json, valid_params)
    app.secret_key = key

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        '<SECRET_KEY> is missing'
    )


def test_call_with_wrong_nasa_credentials(
        route, client, valid_json, valid_jwt, valid_params
):
    with patch('requests.get') as mock_request:
        mock_request.return_value.status_code = HTTPStatus.FORBIDDEN
        response = make_request(client, route, get_header(valid_jwt),
                                valid_json, valid_params)

    assert response.status_code == HTTPStatus.OK
    assert response.json == authorization_errors_expected_payload(
        'Wrong NASA API key'
    )
