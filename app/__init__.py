from flask import Flask
from .extensions import initialize_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    initialize_extensions(app)

    from .controllers.admin_controller import admin_bp
    from .controllers.transaction_controller import transaction_bp
    from .controllers.user_controller import user_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(user_bp)

    return app
