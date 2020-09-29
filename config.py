import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NASA_TOKEN = os.environ.get('NASA_TOKEN')
    APOD_URL = f'https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}'
