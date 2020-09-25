from flask import Flask

from api.get_data import get_request_data_api

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(get_request_data_api, url_prefix='/api/v1.0')

if __name__ == '__main__':
    app.run(debug=True)
