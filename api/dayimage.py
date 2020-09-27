from flask import Blueprint, request, jsonify, current_app

from api.utils import get_apod

dayimage_api = Blueprint('dayimage', __name__)


@dayimage_api.route('/dayimage', methods=['POST'])
def dayimage():
    """
    params:

    save image to folder
    return:
        explanation:
    """
