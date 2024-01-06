# app/manage.py
import os
from flask_script import Manager, Server
from app import create_app
from extensions import initialize_extensions
from swagger import api

app = create_app()
manager = Manager(app)

# Initialize extensions
initialize_extensions(app)

# Register Swagger Blueprint
app.register_blueprint(api.blueprint)

# Add runserver command
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))

if __name__ == '__main__':
    manager.run()
