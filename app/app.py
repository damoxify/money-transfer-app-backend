from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from config import Config
from models.user import User
from models.wallet import Wallet_account
from models.transaction import Transaction
from models.beneficiary import Beneficiary
from controllers.admin_controller import admin_ns
from controllers.transaction_controller import transaction_ns
from controllers.user_controller import user_ns
from extensions import initialize_extensions

app = Flask(__name__)
app.config.from_object(Config)
app.config['app.swagger'] = app.config['SWAGGER_PATH']

initialize_extensions(app)

api = Api(app, version='1.0', title='Money Transfer App API', description='API documentation for the Money Transfer App')

jwt = JWTManager(app)

api.add_namespace(admin_ns)
api.add_namespace(transaction_ns)
api.add_namespace(user_ns)

if __name__ == '__main__':
    app.run(debug=True)