from unittest.mock import patch
from unittest.mock import Mock
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

    @patch('api.dayimage.save_file')
    @patch('os.getcwd')
    @patch('requests.get')
    def test_dayimage_all_is_valid(
            self,
            mock_get,
            mock_os_getcwd,
            mock_get_content
    ):
        mock_os_getcwd.return_value = '/Users/mhonc/Projects/SpaceMaxFlask'
        mock_get.return_value = self.get_mock_data(
            VALID_APOD_RESPONSE_DATA,
            HTTPStatus.OK
        )
        response = self.client.post(
            self.dayimage_endpoint,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.request_content_type
            ),
            json=self.request_params
        )
        expected_result = REQUIRED_DAYIMAGE_RESPONSE_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_dayimage_wrong_jwt(self,):
        response = self.client.post(
            self.dayimage_endpoint,
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
        mock_get.return_value = self.get_mock_data(
            INVALID_APOD_RESPONSE_DATA,
            HTTPStatus.OK
        )
        response = self.client.post(
            self.dayimage_endpoint,
            headers=self.get_headers(
                self.jwt_token,
                content_type=self.request_content_type
            ),
            json=self.request_params
        )
        expected_result = DREQUIRED_AYIMAGE_RESPONSE_INVALID_APOD_DATA

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
