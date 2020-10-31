from unittest.mock import patch
from http import HTTPStatus

from tests_unit.base_test_class import BaseSMFTest
from tests_unit.mocks_requirements_for_tests import (
    VALID_CME_RESPONSE_DATA,
    REQUIRED_CME_RESPONSE_OK,
    REQUIRED_RESPONSE_WRONG_JWT
)


class CMETest(BaseSMFTest):
    cme_endpoint = '/api/v1.0/cme'
    request_params = {'startDate': '2020-09-01', 'endDate': '2020-10-03'}
    wrong_jwt = 'wrong_jwt'

    @patch('requests.get')
    def test_cme_all_is_valid(self, mock_requests):
        mock_requests.return_value = self.get_mock_requests(
            json=VALID_CME_RESPONSE_DATA,
            status=HTTPStatus.OK
        )
        response = self.client.get(
            path=self.cme_endpoint,
            query_string=self.request_params,
            headers=self.get_headers(self.jwt_token)
        )
        expected_result = REQUIRED_CME_RESPONSE_OK

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)

    def test_cme_wrong_jwt(self):
        response = self.client.get(
            path=self.cme_endpoint,
            query_string=self.request_params,
            headers=self.get_headers(self.wrong_jwt)
        )
        expected_result = REQUIRED_RESPONSE_WRONG_JWT

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
