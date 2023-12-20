import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from app.app import create_app, db
from app.models.user import User
from app.models.transaction import Transaction
from app.controllers.transaction_controller import transaction_ns

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/money_transfer_app_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        # Add test data if needed
        user = User(username='test_user', password='test_password')
        db.session.add(user)
        db.session.commit()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def authenticate(client, username, password):
    response = client.post('/api/auth/login', json={'username': username, 'password': password})
    data = response.get_json()
    return data.get('access_token', None)

def test_unauthorized_access(client):
    response = client.get('/api/transactions/list')
    assert response.status_code == 401

def test_authorized_access(client):
    access_token = authenticate(client, 'test_user', 'test_password')
    assert access_token is not None

    headers = {'Authorization': f'Bearer {access_token}'}

    response = client.get('/api/transactions/list', headers=headers)
    assert response.status_code == 200

def test_invalid_credentials(client):
    access_token = authenticate(client, 'invalid_user', 'invalid_password')
    assert access_token is None

    headers = {'Authorization': 'Bearer invalid_token'}
    response = client.get('/api/transactions/list', headers=headers)
    assert response.status_code == 401
