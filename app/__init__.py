from flask import Flask
from config import Config
from extensions import initialize_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['app.swagger'] = app.config['SWAGGER_PATH']

    initialize_extensions(app)

    return app
