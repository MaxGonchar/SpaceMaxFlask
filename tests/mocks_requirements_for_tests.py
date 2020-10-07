VALID_APOD_RESPONSE_DATA = {
    "explanation": "Some explanation",
    "url": "https://domen/adres/image.jpg",
    "hdurl": "https://domen/adres/imagehd.jpg"
}
INVALID_APOD_RESPONSE_DATA = {"explanation": "Something is going wrong"}


REQUIRED_DAYIMAGE_RESPONSE_OK = {
    'explanation': 'Some explanation',
    'message': 'Image successfully downloaded, link:'
               ' /Users/mhonc/Projects/SpaceMaxFlask/tests/media/'
               '2020-09-20_hd.jpg'
}
REQUIRED_DAYIMAGE_RESPONSE_WRONG_JWT = {
            "message": "Invalid input segments length: ",
            "status_code": 500
}
DREQUIRED_AYIMAGE_RESPONSE_INVALID_APOD_DATA = {
            "message": "'url'",
            "status_code": 500
}
