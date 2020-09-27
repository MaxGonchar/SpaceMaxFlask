import requests
import json
from flask import Flask

from api.dayimage import dayimage_api
from api.errors import UnexpectedResponseError

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(dayimage_api, url_prefix='/api/v1.0')


@app.errorhandler(requests.exceptions.ConnectionError)
def connection_error(error):
    return 'There is no connection to server'


@app.errorhandler(requests.exceptions.ConnectTimeout)
def connection_timeout(error):
    return 'Connection timed out'


@app.errorhandler(requests.exceptions.TooManyRedirects)
def too_many_redirects(error):
    return 'Too many redirects'


@app.errorhandler(json.decoder.JSONDecodeError)
def json_decode_error(error):
    return 'Error while receiving data'


@app.errorhandler(requests.exceptions.HTTPError)
def bad_status_code(error):
    return str(error)


@app.errorhandler(UnexpectedResponseError)
def wrong_params_error(error):
    return str(error)


if __name__ == '__main__':
    app.run(debug=True)
