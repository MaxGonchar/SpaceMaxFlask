from flask import Blueprint, request, jsonify, current_app

from api.utils import get_apod, get_jwt, get_json, download_image

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
    #  get_jwt()
    url = current_app.config.get('APOD_URL')
    #  params = get_json()
    params = request.get_json()
    apod_data = get_apod(
        url, params['date'], params['hd']
    )

    explanation = apod_data['explanation']
    link = apod_data['link']

    #  download_image(link, path)

    return jsonify({
        'explanation': explanation,
        'link': link
    })

