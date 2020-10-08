from unittest import TestCase
from unittest.mock import Mock

from authlib.jose import jwt

from app import app


class BaseSMFTest(TestCase):
    jwt_token = None
    secrete_key = 'test'
    encoding_header = {'alg': 'HS256'}
    encoding_payload = {'key': 'NASA_token'}
    request_headers_key = 'Authorization'
    request_headers_value = 'bearer {jwt_token}'

    @classmethod
    def setUpClass(cls) -> None:
        cls.jwt_token = jwt.encode(cls.encoding_header,
                                   cls.encoding_payload,
                                   cls.secrete_key).decode('utf-8')

    def setUp(self) -> None:
        app.secret_key = self.secrete_key
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
            self.request_headers_key: self.request_headers_value.format(
                jwt_token=jwt_token
            )
        }
        if content_type:
            headers['Content-Type'] = content_type
        return headers
