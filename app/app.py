from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from config import Config
from models.user import User
from models.wallet import Wallet_account
from models.transaction import Transaction
from models.beneficiary import Beneficiary
from controllers import user_ns 
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.config.from_object(Config)
app.wsgi_app = ProxyFix(app.wsgi_app)  

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, version='1.0', title='Money Transfer App API', description='API documentation for the Money Transfer App')

api.add_namespace(user_ns)

if __name__ == '__main__':
    app.run(debug=True)
