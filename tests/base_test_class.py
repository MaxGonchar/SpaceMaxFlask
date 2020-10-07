from unittest import TestCase
from unittest.mock import Mock

from authlib.jose import jwt

from app import app


class BaseSMFTest(TestCase):
    jwt_token = None
    SECRETE_KEY = 'test'
    ENCODING_HEADER = {'alg': 'HS256'}
    ENCODING_PAYLOAD = {'key': 'NASA_token'}

    REQUEST_HEADERS_KEY = 'Authorization'
    REQUEST_HEADERS_VALUE = 'bearer {jwt_token}'

    @classmethod
    def setUpClass(cls) -> None:
        cls.jwt_token = jwt.encode(cls.ENCODING_HEADER,
                                   cls.ENCODING_PAYLOAD,
                                   cls.SECRETE_KEY).decode('utf-8')

    def setUp(self) -> None:
        app.secret_key = self.SECRETE_KEY
        self.client = app.test_client()
        self.jwt_token = self.jwt_token

    @staticmethod
    def get_mock_data(data, status):
        mock_data = Mock()
        mock_data.json.return_value = data
        mock_data.status_code = status
        return mock_data

    def get_headers(self, jwt_token: str, content_type=None) -> dict:
        headers = {
            self.REQUEST_HEADERS_KEY: self.REQUEST_HEADERS_VALUE.format(
                jwt_token=jwt_token
            )
        }
        if content_type:
            headers['Content-Type'] = content_type
        return headers
