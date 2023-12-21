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
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
    docs.init_app(app)

    return app
