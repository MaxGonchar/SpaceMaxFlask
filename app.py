from flask import Flask

from api.check_post import check_post_api

app = Flask(__name__)

app.config.from_object('config.Config')

app.register_blueprint(check_post_api, url_prefix='/api/v1.0')

if __name__ == '__main__':
    app.run(debug=True)
