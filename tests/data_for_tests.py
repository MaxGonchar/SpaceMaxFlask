import json


VALID_DATA_IN = {
            'endpoint': '/api/v1.0/dayimage',
            'params': {
                'data': json.dumps({"date": "2020-09-20",
                                    "hd": True}),
                'content_type': 'application/json',
                'headers': {
                    'Authorization': 'bearer '
                                     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                                     'eyJrZXkiOiJrVE1IV01icHdNZ282Qmx4OXJkZ'
                                     'zVIUERNMWhkdjQ3MjJSd0F2eW03In0.Crq5y2a'
                                     'At_5PM4vPQ_dGoPUav4NULWTkyvpBnztmp7E'
                }
            }
        }
# bad jwt
INVALID_DATA_IN = {
            'endpoint': '/api/v1.0/dayimage',
            'params': {
                'data': json.dumps({"date": "2020-09-20",
                                    "hd": True}),
                'content_type': 'application/json',
                'headers': {
                    'Authorization': 'bearer '
                                     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                                     'eyJrZXkiOiJrVE1IV01icHdNZ282Qmx4OXJkZ'
                                     'zVIUERNMWhkdjQ3MjJSd0F2eW03In0.Crq5y2a'
                                     'At_5PM4vPQ_dGoPUav4NULWTkyvpBnztmp7Ep'
                }
            }
        }
VALID_MOCK_DATA = {
            'response': {
                "explanation": "Some explanation",
                "url": "https://domen/adres/image.jpg",
                "hdurl": "https://domen/adres/imagehd.jpg"
            },
            'status_code': 200
        }
INVALID_MOCK_DATA = {
            'response': {
                "explanation": "Something is going wrong",
            },
            'status_code': 200
        }

REQUIRED_TEST_DAYIMAGE_ALL_IS_VALID = {
            'explanation': 'Some explanation',
            'message': 'Image successfully downloaded, link:'
                       ' /Users/mhonc/Projects/SpaceMaxFlask/media/'
                       '2020-09-20_hd.jpg'
        }
REQUIRED_TEST_DAYIMAGE_WRONG_JWT = {
            "message": "bad_signature: ",
            "status_code": 500
        }
REQUIRED_TEST_DAYIMAGE_WRONG_APOD_DATA = {
            "message": "'url'",
            "status_code": 500
        }
