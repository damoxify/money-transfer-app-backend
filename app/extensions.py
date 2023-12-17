from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.app import app

db = SQLAlchemy()
migrate = Migrate(app, db)
cors = CORS()
jwt = JWTManager()

def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
   
    return app
