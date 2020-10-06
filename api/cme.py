import requests
from flask import Blueprint, jsonify, current_app, request

from api.utils import get_cme, get_jwt, get_params, url_for


cme_api = Blueprint('cme', __name__)


@cme_api.route('/cme', methods=['GET'])
def cme():
    # params = {'api_key': get_jwt(), **get_params()}
    # cme_data = get_cme(
    #     url_for(current_app.config.get('NASA_ENDPOINTS')['cme']), params
    # )
    print(request.method)
    return jsonify({'message': 'HI!'})
