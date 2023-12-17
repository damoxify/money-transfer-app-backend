from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
jwt = JWTManager()

def initialize_extensions(run):
    db.init_app(run)
    migrate.init_app(run, db)
    cors.init_app(run)
    jwt.init_app(run)
   
    return run
