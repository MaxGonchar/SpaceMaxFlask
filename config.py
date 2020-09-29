import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    NASA_API = 'https://api.nasa.gov{path}'
