from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.app import create_app, db
from app.swagger import swagger_namespace

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))

app.register_blueprint(swagger_namespace, url_prefix='/swagger')

if __name__ == '__main__':
    manager.run()
