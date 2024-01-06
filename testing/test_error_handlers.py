import pytest
from flask import Flask
from flask.testing import FlaskClient
from app.app import create_app, db
from app.models.user import User
from app.models.transaction import Transaction
from app.controllers.admin_controller import admin_ns
from app.controllers.transaction_controller import transaction_ns
from app.controllers.user_controller import user_ns

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

