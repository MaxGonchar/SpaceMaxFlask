from unittest.mock import patch
from http import HTTPStatus

from tests.base_test_class import BaseSMFTest
from tests.mocks_requirements_for_tests import (
    VALID_APOD_RESPONSE_DATA,
    INVALID_APOD_RESPONSE_DATA,

    REQUIRED_DAYIMAGE_RESPONSE_OK,
    REQUIRED_DAYIMAGE_RESPONSE_WRONG_JWT,
    DREQUIRED_AYIMAGE_RESPONSE_INVALID_APOD_DATA
)


@patch('api.dayimage.download_file')
@patch('api.dayimage.save_file')
@patch('requests.get')
class DayImageTest(BaseSMFTest):
    DAYIMAGE_ENDPOINT = '/api/v1.0/dayimage'
    REQUEST_PARAMS = {"date": "2020-09-20", "hd": True}
    REQUEST_CONTENT_TYPE = 'application/json'
    WRONG_JWT = 'wrong_jwt'

    def test_dayimage_all_is_valid(
            self,
            mock_get,
            mock_save_file,
            mock_download_file
    ):
        mock_get.return_value = self.get_mock_data(
            VALID_APOD_RESPONSE_DATA,
            HTTPStatus.OK
        )

        response = self.client.post(
            self.DAYIMAGE_ENDPOINT,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.REQUEST_CONTENT_TYPE
            ),
            json=self.REQUEST_PARAMS
        )
        expected_result = REQUIRED_DAYIMAGE_RESPONSE_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_dayimage_wrong_jwt(
            self,
            mock_get,
            mock_save_file,
            mock_download_file
    ):
        mock_get.return_value = self.get_mock_data(
            VALID_APOD_RESPONSE_DATA,
            HTTPStatus.OK
        )

        response = self.client.post(
            self.DAYIMAGE_ENDPOINT,
            headers=self.get_headers(
                self.WRONG_JWT,
                content_type=self.REQUEST_CONTENT_TYPE
            ),
            json=self.REQUEST_PARAMS,
        )
        expected_result = REQUIRED_DAYIMAGE_RESPONSE_WRONG_JWT

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_dayimage_invalid_apod_data(
            self,
            mock_get,
            mock_save_file,
            mock_download_file
    ):
        mock_get.return_value = self.get_mock_data(
            INVALID_APOD_RESPONSE_DATA,
            HTTPStatus.OK
        )

        response = self.client.post(
            self.DAYIMAGE_ENDPOINT,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.REQUEST_CONTENT_TYPE
            ),
            json=self.REQUEST_PARAMS
        )
        expected_result = DREQUIRED_AYIMAGE_RESPONSE_INVALID_APOD_DATA

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
