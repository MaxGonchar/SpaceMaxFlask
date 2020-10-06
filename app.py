from http import HTTPStatus

import requests
from flask import Flask, jsonify

from api.dayimage import dayimage_api
from api.cme import cme_api
from api.errors import SMFError

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(dayimage_api, url_prefix='/api/v1.0')
app.register_blueprint(cme_api, url_prefix='/api/v1.0')


@app.errorhandler(SMFError)
def handle_cred_error(error):
    app.logger.exception(error)
    return jsonify(error.json())


@app.errorhandler(Exception)
def handle_error(error):
    app.logger.exception(error)

    if isinstance(error, requests.exceptions.HTTPError):
        status_code = error.response.status_code
        message = f'{error.response.reason} for url {error.response.url}'
    else:
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        message = str(error)

    return jsonify({
        'status_code': status_code,
        'message': message
    })


if __name__ == '__main__':
    app.run(debug=True)
