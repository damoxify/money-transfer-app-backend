# extensions.py
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_apispec import FlaskApiSpec

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
jwt = JWTManager()
docs = FlaskApiSpec()

def initialize_extensions(app):
    # Initialize extensions only if not initialized before
    if not hasattr(app, 'extensions_initialized'):
        app.extensions_initialized = True

        db.init_app(app)
        migrate.init_app(app, db)
        cors.init_app(app)
        jwt.init_app(app)

        # Create a regular Flask blueprint with a unique name
        api_docs_blueprint = Blueprint('api_docs_blueprint', __name__, url_prefix='/api/docs')

        # Register the blueprint with the app
        app.register_blueprint(api_docs_blueprint)

        # Initialize Flask-APISpec with the app
        docs.init_app(app)

        # Manually add the paths from the blueprint to Flask-APISpec
        for rule in app.url_map.iter_rules():
            if rule.endpoint == 'api_docs_blueprint':
                docs.register(app, rule=rule)

    return app
