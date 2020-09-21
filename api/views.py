from flask import request, jsonify

from api import app
from api.api_utils import get_payload


@app.route('/api/v1.0/post', methods=['POST'])
def get_credentials():
    token = bytes(request.headers['payload'], 'utf-8')
    body = request.json
    payload = get_payload(token)
    return jsonify({'payload': payload, 'body': body})
