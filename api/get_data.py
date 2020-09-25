from flask import Blueprint

get_request_data_api = Blueprint('get_request_data', __name__)


@get_request_data_api.route('/get_request_data', methods=['POST'])
def get_request_data():
    """
    params:

    save image to folder
    return:
        explanation:
    """
