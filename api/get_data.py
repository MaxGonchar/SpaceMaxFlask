from flask import Blueprint, jsonify, request

from api.validation import jwt_valid, json_valid

get_request_data_api = Blueprint('get_request_data', __name__)


@get_request_data_api.route('/get_request_data', methods=['POST'])
def get_request_data():
    """
    params:

    save image to folder
    return:
        explanation:
    """
    if jwt_valid():
        data = request.get_json()
    else:
        return jsonify({'Error': 'Bad Authentication data'})
