import os
from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager, Server
from app import create_app, db
from app.extensions import initialize_extensions, docs
from app.swagger import swagger_namespace, SwaggerResource

app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('runserver', Server(host='127.0.0.1', port=5000))
initialize_extensions(app)
app.register_blueprint(swagger_namespace, url_prefix='/swagger')

if __name__ == '__main__':
    manager.run()
