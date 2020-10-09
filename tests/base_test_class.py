from unittest import TestCase
from unittest.mock import Mock

from authlib.jose import jwt

from app import app


class BaseSMFTest(TestCase):
    jwt_token = None
    secrete_key = 'test'
    encoding_header = {'alg': 'HS256'}
    encoding_payload = {'key': 'NASA_token'}

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
    def get_mock_requests(json=None, status=None, content=None):
        mock_data = Mock()
        if json:
            mock_data.json.return_value = json
        if status:
            mock_data.status_code = status
        if content:
            mock_data.content = content
        return mock_data

    def get_headers(self, jwt_token: str, content_type=None) -> dict:
        headers = {'Authorization': f'bearer {jwt_token}'}
        if content_type:
            headers['Content-Type'] = content_type
        return headers
