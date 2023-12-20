import os
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import app, db

migrate = Migrate(app, db)
manager = FlaskGroup(app)

if __name__ == '__main__':
    manager.run()
