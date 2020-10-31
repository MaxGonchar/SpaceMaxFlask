from http import HTTPStatus

from pytest import fixture

from api.errors import AUTH_ERROR
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


def test_call_with_wrong_authorization_type():
    pass


def test_call_with_wrong_jwt_structure():
    pass


def test_call_with_wrong_jwt_payload_structure():
    pass


def test_call_with_jwt_encoded_wrong_key():
    pass


def test_call_with_no_secret_key():
    pass


def test_call_with_wrong_nasa_credentials():
    pass
