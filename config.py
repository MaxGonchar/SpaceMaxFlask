import os

from genersl_utils import read_key

SECRET_KEY = os.environ.get('SECRET_KEY') or read_key('key.pub')
