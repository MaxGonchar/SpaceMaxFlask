from flask import Blueprint, request, jsonify, current_app

from api.utils import get_apod, get_json, get_jwt, download_image

dayimage_api = Blueprint('dayimage', __name__)


@dayimage_api.route('/dayimage', methods=['POST'])
def dayimage():
    """
    params:

    save image to folder
    return:
        explanation:
    """
    url = current_app.config.get('APOD_URL')
    # get_jwt() - will be later
    # params = get_json() - will be later
    # temporary, until I have not get_json()
    params = request.get_json()
    data = get_apod(
        url, params['date'], params['hd']
    )
    # download_image() - will be later
    return jsonify(data)
