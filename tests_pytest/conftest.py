from authlib.jose import jwt
from pytest import fixture

from app import app


@fixture(scope='session')
def client():
    app.testing = True
    client = app.test_client()
    client.application.secret_key = 'test_key'
    return client


@fixture(scope='session')
def valid_jwt():
    header = {'alg': 'HS256'}
    payload = {'key': 'some_key'}
    key = app.secret_key
    return jwt.encode(header, payload, key).decode('ascii')


@fixture(scope='session')
def valid_json():
    return {
        'date': '2020-09-20',
        'hd': True
    }


@fixture(scope='session')
def valid_params():
    return {
        'startDate': '2020-09-30',
        'endDate': '2020-10-03'
    }
