import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    NASA_API = 'https://api.nasa.gov/{endpoint}'

    NASA_ENDPOINTS = {
        'apod': 'planetary/apod',
        'cme': 'DONKI/CME'
    }

    MEDIA_FOLDER = 'media'
