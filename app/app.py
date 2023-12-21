from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from controllers.admin_controller import admin_bp
from controllers.transaction_controller import transaction_bp
from controllers.user_controller import user_bp
from extensions import initialize_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['app.swagger'] = app.config['SWAGGER_PATH']

    initialize_extensions(app)

    app.register_blueprint(admin_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(user_bp)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
