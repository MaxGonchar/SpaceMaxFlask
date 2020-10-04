from requests import Response
import unittest
from unittest.mock import patch, Mock
import sys

sys.path.insert(0, '/Users/mhonc/Projects/SpaceMaxFlask')

from app import app
from tests.data_for_tests import (
    VALID_DATA_IN,
    INVALID_DATA_IN,
    VALID_MOCK_DATA,
    INVALID_MOCK_DATA,
    REQUIRED_TEST_DAYIMAGE_ALL_IS_VALID,
    REQUIRED_TEST_DAYIMAGE_WRONG_JWT,
    REQUIRED_TEST_DAYIMAGE_WRONG_APOD_DATA
)


def get_params_for_tests():
    yield {
        'data_in': VALID_DATA_IN,
        'data_out': REQUIRED_TEST_DAYIMAGE_ALL_IS_VALID,
        'mock_data': VALID_MOCK_DATA
    }
    yield {
        'data_in': INVALID_DATA_IN,
        'data_out': REQUIRED_TEST_DAYIMAGE_WRONG_JWT,
        'mock_data': VALID_MOCK_DATA
    }
    yield {
        'data_in': VALID_DATA_IN,
        'data_out': REQUIRED_TEST_DAYIMAGE_WRONG_APOD_DATA,
        'mock_data': INVALID_MOCK_DATA
    }


params_for_test = get_params_for_tests()


class SpaceMaxFlask(unittest.TestCase):

    @staticmethod
    def get_mock_data(data):
        mock_data = Mock(Response)
        mock_data.json.return_value = data['mock_data'][
            'response']
        mock_data.status_code = data['mock_data']['status_code']
        return mock_data

    def setUp(self) -> None:
        app.secret_key = 'test'
        test_data = next(params_for_test)

        self.patcher1 = patch('api.dayimage.download_file')
        mock_download_file = self.patcher1.start()

        self.patcher2 = patch('api.dayimage.save_file')
        mock_save_file = self.patcher2.start()

        self.patcher3 = patch('requests.get')
        mock_get = self.patcher3.start()
        mock_get.return_value = self.get_mock_data(test_data)

        self.response = app.test_client().post(
            test_data['data_in']['endpoint'],
            **test_data['data_in']['params']
        )

        self.expected_result = test_data['data_out']

    def tearDown(self) -> None:
        self.patcher1.stop()
        self.patcher2.stop()
        self.patcher3.stop()

    def test_dayimage_all_is_valid(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json, self.expected_result)

    def test_dayimage_wrong_jwt(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json, self.expected_result)

    def test_dayimage_wrong_apod_data(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json, self.expected_result)


if __name__ == '__main__':
    unittest.main()
