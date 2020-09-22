import os

from genersl_utils import read_key


class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SECRET_KEY = read_key('key.pub')
