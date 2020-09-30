from flask import Blueprint, jsonify, current_app

from api.utils import get_apod, get_jwt, get_json, download_image, url_for
from api.schemas import APODParamsSchema

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
    params = {'api_key': get_jwt(), **get_json(APODParamsSchema())}
    apod_data = get_apod(
        url_for(current_app.config.get('NASA_ENDPOINTS')['apod']), params
    )

    #  link can be not only to image, for example, to video in youtube.
    if apod_data['link'].endswith('.jpg'):
        name = params['date'] + '_hd' if params['hd'] else params['date']
        download_image(apod_data['link'], name)
        message = 'image successfully downloaded'
    else:
        message = f"There are no jpg images on the date indicated, " \
                  f"the material can be found at the link {apod_data['link']}"

    return jsonify({
        'explanation': apod_data['explanation'],
        'message': message
    })

