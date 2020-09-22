from flask import request, jsonify, Blueprint

from api.utils import get_payload

post_api = Blueprint('post', __name__)


@post_api.route('/post', methods=['POST'])
def get_credentials():
    token = request.headers['Authorization'].split()[1]
    body = request.get_json()
    payload = get_payload(token)
    return jsonify({'payload': payload, 'body': body})
