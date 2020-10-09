from flask import Blueprint, jsonify, current_app

from api.utils import (
    get_nasa_data,
    get_jwt,
    get_params,
    url_for,
    get_path_to_save,
    download_file,
    save_file
)
from api.schemas import APODParamsSchema

dayimage_api = Blueprint('dayimage', __name__)

IMAGE_DOWNLOADED = 'Image successfully downloaded, link: {link}'
IMAGE_NOT_FOUND = 'There are no jpg images on the date indicated,'  \
           'the material can be found at the link {link}'


def form_apod_data(data: dict, hd: bool) -> dict:
    """
    Form correct message for dayimage endpoint if nasa API has provided it
    params:
        data: data from nasa API
        hd: hit definition of image (True/False)
    return:
        dict with info.
    """
    if not data.get('Sorry'):
        # not in all day's json 'hdurl' exists
        link = data['hdurl'] if hd and data.get('hdurl') else data['url']
        return {
            'explanation': data['explanation'],
            'link': link
        }
    return data


@dayimage_api.route('/dayimage', methods=['POST'])
def dayimage():
    """
    get from NASA-APOD link to video resource and explanation
    if resource is image, save it to folder, otherwise return only link
    return:
        explanation: text followed with media resource
        message: about resource and actions with it if there was.
    """
    params = {'api_key': get_jwt(), **get_params(APODParamsSchema())}
    nasa_data = get_nasa_data(
        url_for(current_app.config.get('NASA_ENDPOINTS')['apod']),
        params
    )
    apod_data = form_apod_data(nasa_data, params['hd'])

    #  link can be not only to image, for example, to video in youtube.
    if apod_data['link'].endswith('.jpg'):
        name = params['date'] + '_hd' if params['hd'] else params['date']
        save_file(
            path=get_path_to_save(name),
            data=download_file(apod_data['link'])
        )
        message = IMAGE_DOWNLOADED.format(link=get_path_to_save(name))
    else:
        message = IMAGE_NOT_FOUND.format(link=apod_data['link'])

    return jsonify({
        'explanation': apod_data['explanation'],
        'message': message
    })
