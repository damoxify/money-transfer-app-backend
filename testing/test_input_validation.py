import pytest
from app.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_invalid_transaction_amount(client):
    response = client.post('/api/transaction', json={'amount': 'invalid_amount'})
    assert response.status_code == 400
    assert 'Invalid transaction amount' in response.get_json().get('error')

def test_missing_username(client):
    response = client.post('/api/user', json={})
    assert response.status_code == 400
    assert 'Username is required' in response.get_json().get('error')

def test_invalid_email_format(client):
    response = client.post('/api/user', json={'username': 'test_user', 'email': 'invalid_email'})
    assert response.status_code == 400
    assert 'Invalid email format' in response.get_json().get('error')
