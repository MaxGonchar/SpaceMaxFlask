import builtins
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


class DayImageTest(BaseSMFTest):
    dayimage_endpoint = '/api/v1.0/dayimage'
    request_params = {"date": "2020-09-20", "hd": True}
    request_content_type = 'application/json'
    wrong_jwt = 'wrong_jwt'

    @patch('builtins.open')
    @patch('os.getcwd')
    @patch('requests.get')
    def test_dayimage_all_is_valid(self, mock_requests, mock_os_getcwd,
                                   mosk_open):
        mock_os_getcwd.return_value = '/Users/mhonc/Projects/SpaceMaxFlask'
        mock_requests.side_effect = [
            self.get_mock_requests(
                json=VALID_APOD_RESPONSE_DATA,
                status=HTTPStatus.OK
            ),
            self.get_mock_requests(content=b'picture')
        ]

        response = self.client.post(
            path=self.dayimage_endpoint,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.request_content_type
            ),
            json=self.request_params
        )
        expected_result = REQUIRED_DAYIMAGE_RESPONSE_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_dayimage_wrong_jwt(self):
        response = self.client.post(
            path=self.dayimage_endpoint,
            headers=self.get_headers(
                self.wrong_jwt,
                content_type=self.request_content_type
            ),
            json=self.request_params,
        )
        expected_result = REQUIRED_DAYIMAGE_RESPONSE_WRONG_JWT

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    @patch('requests.get')
    def test_dayimage_invalid_apod_data(self, mock_get):
        mock_get.return_value = self.get_mock_requests(
            json=INVALID_APOD_RESPONSE_DATA,
            status=HTTPStatus.OK
        )
        response = self.client.post(
            path=self.dayimage_endpoint,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.request_content_type
            ),
            json=self.request_params
        )
        expected_result = DREQUIRED_AYIMAGE_RESPONSE_INVALID_APOD_DATA

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
