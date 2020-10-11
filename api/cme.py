from flask import Blueprint, jsonify, current_app

from api.schemas import CMEParamsSchema
from api.utils import (
    get_jwt,
    get_params,
    url_for,
    get_nasa_data
)

cme_api = Blueprint('cme', __name__)


def form_cme_data(data):
    """
    Form correct message for cme endpoint if nasa API has provided it
    params:
        data: data from nasa API
    return:
        dict with info.
    """
    if isinstance(data, list):
        res = [{'coronalMassEjectionQuantity': len(data)}, []]
        for el in data:
            res[1].append({
                'startTime': el['startTime'],
                'explanation': el['note'],
                'link to DONKI': el['link']
            })
        return res
    return data


@cme_api.route('/cme', methods=['GET'])
def cme():
    """
    Get from NASA DONKI CME info about coronal mass ejections in specified
    period.
    Return number of ejections if there were;
    start time for each;
    short description;
    link to Space Weather Database Of Notifications for each.
    """
    params = {'api_key': get_jwt(), **get_params(CMEParamsSchema())}
    nasa_data = get_nasa_data(
        url_for(current_app.config.get('NASA_ENDPOINTS')['cme']),
        params
    )
    cme_data = form_cme_data(nasa_data)
    return jsonify(cme_data)
