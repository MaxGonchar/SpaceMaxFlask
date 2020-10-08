import requests
from flask import Blueprint, jsonify, current_app, request

from api.schemas import CMEParamsSchema
from api.utils import get_jwt, get_params, url_for, get_apod


cme_api = Blueprint('cme', __name__)


@cme_api.route('/cme', methods=['GET'])
def cme():
    params = {'api_key': get_jwt(), **get_params(CMEParamsSchema)}
    cme_data = get_apod(
        url_for(current_app.config.get('NASA_ENDPOINTS')['cme']),
        params,
        'cme'
    )
    return jsonify(cme_data)
