from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restplus import Api

db = SQLAlchemy()
cors = CORS()
jwt = JWTManager()
api = Api(version='1.0', title='Money Transfer App API', description='API documentation for the Money Transfer App')


def initialize_extensions(app):
    db.init_app(app)
    Migrate(app, db) 
    cors.init_app(app)
    jwt.init_app(app)
    api.init_app(app)
   
    return app
