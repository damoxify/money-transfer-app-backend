#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


from models import db, User, WalletAccount, Beneficiary, Transaction

migrate = Migrate(app, db)


db.init_app(app)


@app.route('/')
def home():
    return '<h1>Money Transfer App API</h1>'



# User-related routes
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    user_dict = new_user.to_dict()
    return make_response(jsonify(user_dict), 201)


@app.route('/users/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def manage_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify(message="User not found"), 404

    if request.method == 'GET':
        user_dict = user.to_dict()
        return make_response(jsonify(user_dict), 200)

    elif request.method == 'PATCH':
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        user_dict = user.to_dict()
        return make_response(jsonify(user_dict), 200)

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify(message="User deleted"), 200




# Wallet Account-related routes
@app.route('/wallets', methods=['POST'])
def create_wallet_account():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)
    
    if user is None:
        return jsonify(message="User not found"), 404
    
    new_wallet_account = WalletAccount(**data)
    user.wallet_accounts.append(new_wallet_account)
    
    db.session.commit()
    
    wallet_account_dict = new_wallet_account.to_dict()
    return make_response(jsonify(wallet_account_dict), 201)





# Beneficiary-related routes
@app.route('/beneficiaries', methods=['POST'])
def add_beneficiary():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)

    if user is None:
        return jsonify(message="User not found"), 404

    new_beneficiary = Beneficiary(**data)
    user.beneficiaries.append(new_beneficiary)

    db.session.commit()

    beneficiary_dict = new_beneficiary.to_dict()
    return make_response(jsonify(beneficiary_dict), 201)

@app.route('/beneficiaries/<int:beneficiary_id>', methods=['GET', 'PATCH', 'DELETE'])
def manage_beneficiary(beneficiary_id):
    beneficiary = Beneficiary.query.get(beneficiary_id)
    if beneficiary is None:
        return jsonify(message="Beneficiary not found"), 404

    if request.method == 'GET':
        beneficiary_dict = beneficiary.to_dict()
        return make_response(jsonify(beneficiary_dict), 200)

    elif request.method == 'PATCH':
        data = request.get_json()
        for key, value in data.items():
            setattr(beneficiary, key, value)
        db.session.commit()
        beneficiary_dict = beneficiary.to_dict()
        return make_response(jsonify(beneficiary_dict), 200)

    elif request.method == 'DELETE':
        db.session.delete(beneficiary)
        db.session.commit()
        return jsonify(message="Beneficiary deleted"), 200






# Transaction-related routes
@app.route('/transactions', methods=['POST'])
def make_transaction():
    data = request.get_json()
    user_id = data.get('user_id')
    user = User.query.get(user_id)

    if user is None:
        return jsonify(message="User not found"), 404

    beneficiary_id = data.get('beneficiary_id')
    beneficiary = Beneficiary.query.get(beneficiary_id)

    if beneficiary is None:
        return jsonify(message="Beneficiary not found"), 404

    new_transaction = Transaction(**data)
    user.transactions.append(new_transaction)

    db.session.commit()

    transaction_dict = new_transaction.to_dict()
    return make_response(jsonify(transaction_dict), 201)

@app.route('/transactions/<int:transaction_id>', methods=['GET', 'PATCH', 'DELETE'])
def manage_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if transaction is None:
        return jsonify(message="Transaction not found"), 404

    if request.method == 'GET':
        transaction_dict = transaction.to_dict()
        return make_response(jsonify(transaction_dict), 200)

    elif request.method == 'PATCH':
        data = request.get_json()
        for key, value in data.items():
            setattr(transaction, key, value)
        db.session.commit()
        transaction_dict = transaction.to_dict()
        return make_response(jsonify(transaction_dict), 200)

    elif request.method == 'DELETE':
        db.session.delete(transaction)
        db.session.commit()
        return jsonify(message="Transaction deleted"), 200



if __name__ == '__main__':
    app.run(port=5555, debug=True)
