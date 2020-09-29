from flask import Blueprint, request, jsonify, current_app

from api.utils import get_apod, get_jwt, get_json, download_image, url_for

dayimage_api = Blueprint('dayimage', __name__)


@dayimage_api.route('/dayimage', methods=['POST'])
def dayimage():
    """
    get from NASA-APOD link to image and explanation
    save image to folder
    return:
        explanation:
        link:
    """
    params = {'api_key': get_jwt(), **request.get_json()}
    apod_data = get_apod(url_for('planetary/apod'), params)

    return jsonify({
        'explanation': apod_data['explanation'],
        'link': apod_data['link']
    })

