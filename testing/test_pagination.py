import pytest
from flask import Flask
from flask.testing import FlaskClient
from app.app import create_app, db
from app.models.transaction import Transaction
from app.controllers.transaction_controller import transaction_ns
from app.pagination.pagination import Pagination

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/money_transfer_app_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    with app.app_context():
        db.create_all()

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def pagination():
    return Pagination()

def test_pagination(client, pagination):
  
    response = client.get('/api/transactions/list')
    data = response.get_json()

    assert response.status_code == 200
    assert 'transactions' in data
    assert 'pagination' in data
    assert data['pagination']['page'] == 1
    assert data['pagination']['total_pages'] >= 1
    assert data['pagination']['total_items'] >= 0

    # Test pagination with custom values
    response = client.get('/api/transactions/list?page=2&per_page=5')
    data = response.get_json()

    assert response.status_code == 200
    assert 'transactions' in data
    assert 'pagination' in data
    assert data['pagination']['page'] == 2
    assert data['pagination']['total_pages'] >= 1
    assert data['pagination']['total_items'] >= 0
    assert len(data['transactions']) <= 5  
