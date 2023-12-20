from flask import Flask
from flask.testing import FlaskClient
import pytest
from app import db  
from app.controllers.admin_controller import admin_ns
from app.controllers.transaction_controller import transaction_ns
from app.controllers.user_controller import user_ns
from app.models.transaction import Transaction
from app.models.user import User

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/money_transfer_app_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(admin_ns)
    app.register_blueprint(transaction_ns)
    app.register_blueprint(user_ns)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_list_all_transactions(client):
    response = client.get('/admin/transactions')
    assert response.status_code == 200
    assert 'transactions' in response.json

def test_list_all_users(client):
    response = client.get('/admin/users')
    assert response.status_code == 200
    assert 'users' in response.json

def test_list_transactions(client):
    response = client.get('/transaction/list')
    assert response.status_code == 200
    assert 'transactions' in response.json

def test_list_users(client):
    response = client.get('/user/list')
    assert response.status_code == 200
    assert 'users' in response.json
