import json
from http import HTTPStatus

SECRETE_KEY = 'test'
ENCODING_HEADER = {'alg': 'HS256'}
ENCODING_PAYLOAD = {'key': 'NASA_token'}

VALID_APOD_RESPONSE_STATUS = HTTPStatus.OK
VALID_APOD_RESPONSE_DATA = {
    "explanation": "Some explanation",
    "url": "https://domen/adres/image.jpg",
    "hdurl": "https://domen/adres/imagehd.jpg"}
INVALID_APOD_RESPONSE_DATA = {"explanation": "Something is going wrong"}

DAYIMAGE_ENDPOINT = '/api/v1.0/dayimage'
REQUEST_PARAMS = json.dumps({"date": "2020-09-20", "hd": True})
REQUEST_CONTENT_TYPE = 'application/json'
REQUEST_HEADERS_KEY = 'Authorization'
REQUEST_HEADERS_VALUE = 'bearer {jwt_token}'
REQUEST_HEADERS_VALUE_WRONG_JWT = 'bearer wrong_jwt'

DAYIMAGE_RESPONSE_OK = {
    'explanation': 'Some explanation',
    'message': 'Image successfully downloaded, link:'
               ' /Users/mhonc/Projects/SpaceMaxFlask/tests/media/'
               '2020-09-20_hd.jpg'}
DAYIMAGE_RESPONSE_AFTER_WRONG_JWT = {
            "message": "Invalid input segments length: ",
            "status_code": 500}
DAYIMAGE_RESPONSE_AFTER_INVALID_APOD_DATA = {
            "message": "'url'",
            "status_code": 500}
