from unittest import TestCase
from unittest.mock import patch, Mock

from authlib.jose import jwt

from app import app
from tests.data_for_tests import (
    SECRETE_KEY,
    ENCODING_HEADER,
    ENCODING_PAYLOAD,

    VALID_APOD_RESPONSE_STATUS,
    VALID_APOD_RESPONSE_DATA,
    INVALID_APOD_RESPONSE_DATA,

    DAYIMAGE_ENDPOINT,
    REQUEST_PARAMS,
    REQUEST_CONTENT_TYPE,
    REQUEST_HEADERS_KEY,
    REQUEST_HEADERS_VALUE,
    REQUEST_HEADERS_VALUE_WRONG_JWT,

    DAYIMAGE_RESPONSE_OK,
    DAYIMAGE_RESPONSE_AFTER_WRONG_JWT,
    DAYIMAGE_RESPONSE_AFTER_INVALID_APOD_DATA
)


class DayImageTest(TestCase):
    jwt_token = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.jwt_token = jwt.encode(ENCODING_HEADER,
                                   ENCODING_PAYLOAD,
                                   SECRETE_KEY).decode('utf-8')

    def setUp(self) -> None:
        app.secret_key = SECRETE_KEY
        self.client = app.test_client()
        self.jwt_token = DayImageTest.jwt_token

    @staticmethod
    def get_mock_data(data, status):
        mock_data = Mock()
        mock_data.json.return_value = data
        mock_data.status_code = status
        return mock_data

    @patch('api.dayimage.download_file')
    @patch('api.dayimage.save_file')
    @patch('requests.get')
    def test_dayimage_all_is_valid(
            self,
            mock_get,
            mock_save_file,
            mock_download_file
    ):
        mock_get.return_value = self.get_mock_data(
            VALID_APOD_RESPONSE_DATA,
            VALID_APOD_RESPONSE_STATUS
        )

        response = self.client.post(
            DAYIMAGE_ENDPOINT,
            data=REQUEST_PARAMS,
            content_type=REQUEST_CONTENT_TYPE,
            headers={REQUEST_HEADERS_KEY: REQUEST_HEADERS_VALUE.format(
                jwt_token=self.jwt_token
            )}
        )
        expected_result = DAYIMAGE_RESPONSE_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    @patch('api.dayimage.download_file')
    @patch('api.dayimage.save_file')
    @patch('requests.get')
    def test_dayimage_wrong_jwt(
            self,
            mock_get,
            mock_save_file,
            mock_download_file
    ):
        mock_get.return_value = self.get_mock_data(
            VALID_APOD_RESPONSE_DATA,
            VALID_APOD_RESPONSE_STATUS
        )

        response = self.client.post(
            DAYIMAGE_ENDPOINT,
            data=REQUEST_PARAMS,
            content_type=REQUEST_CONTENT_TYPE,
            headers={REQUEST_HEADERS_KEY: REQUEST_HEADERS_VALUE_WRONG_JWT}
        )
        expected_result = DAYIMAGE_RESPONSE_AFTER_WRONG_JWT

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    @patch('api.dayimage.download_file')
    @patch('api.dayimage.save_file')
    @patch('requests.get')
    def test_dayimage_invalid_apod_data(
            self,
            mock_get,
            mock_save_file,
            mock_download_file
    ):
        mock_get.return_value = self.get_mock_data(
            INVALID_APOD_RESPONSE_DATA,
            VALID_APOD_RESPONSE_STATUS
        )

        response = self.client.post(
            DAYIMAGE_ENDPOINT,
            data=REQUEST_PARAMS,
            content_type=REQUEST_CONTENT_TYPE,
            headers={REQUEST_HEADERS_KEY: REQUEST_HEADERS_VALUE.format(
                jwt_token=self.jwt_token
            )}
        )
        expected_result = DAYIMAGE_RESPONSE_AFTER_INVALID_APOD_DATA

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
