#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask import request, jsonify, g
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


from models import db, User, WalletAccount, Beneficiary, Transaction

migrate = Migrate(app, db)


db.init_app(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return '<h1>Money Transfer App API</h1>'



# User-related routes
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    required_fields = ['username', 'fullname', 'email', 'password']
    if not all(field in data for field in required_fields):
        return jsonify(message="Missing required fields"), 400

    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify(message="User with this email already exists"), 409

    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

    data['password'] = hashed_password
    data['registered_on'] = datetime.utcnow()

    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    
    user_dict = new_user.to_dict()
    return make_response(jsonify(user_dict), 201)



@app.route('/users/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def modify_user(user_id):
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

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            user.is_authenticated = True
            db.session.commit()

            access_token = create_access_token(identity=user.id)

            return jsonify({"message": "Login successful", "access_token": access_token, "user": user.to_dict()}), 200
        else:
            return jsonify({"message": "Invalid email or password"}), 401

    except Exception as e:
        print(e)
        return jsonify({"message": "Internal server error"}), 500


@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)

        if user:
            user.is_authenticated = False
            db.session.commit()


            return jsonify({"message": "Logout successful"}), 200
        else:
            return jsonify({"message": "User not found"}), 404

    except Exception as e:
        print(e)
        return jsonify({"message": "Internal server error"}), 500




# Admin-related routes
@app.route('/admin/users', methods=['GET', 'POST'])
def add_users():
    if request.method == 'GET':
        try:
            users = User.query.all()
            users_list = [user.to_dict() for user in users]
            return make_response(jsonify(users_list), 200)
        except Exception as e:
            return make_response(jsonify(message="Error retrieving users"), 500)

    elif request.method == 'POST':
        try:
            data = request.get_json()

            if not all(key in data for key in ['username', 'password', 'fullname', 'email']):
                return make_response(jsonify(message="Incomplete user data"), 400)

            new_user = User(**data)
            db.session.add(new_user)
            db.session.commit()
            user_dict = new_user.to_dict()
            return make_response(jsonify(user_dict), 201)
        except Exception as e:
            return make_response(jsonify(message="Error creating user"), 500)


@app.route('/admin/users/<int:user_id>', methods=['GET', 'PUT'])
def manage_user(user_id):
    if request.method == 'GET':
        try:
            user = User.query.get(user_id)
            if user:
                user_dict = user.to_dict()
                return make_response(jsonify(user_dict), 200)
            else:
                return make_response(jsonify(message="User not found"), 404)
        except Exception as e:
            return make_response(jsonify(message="Error retrieving user"), 500)

    elif request.method == 'PUT':
        try:
            data = request.get_json()

            if not all(key in data for key in ['username', 'password', 'fullname', 'email']):
                return make_response(jsonify(message="Incomplete user data"), 400)

            user = User.query.get(user_id)

            if user:
                user.username = data['username']
                user.password = data['password']
                user.fullname = data['fullname']
                user.email = data['email']

                db.session.commit()

                user_dict = user.to_dict()
                return make_response(jsonify(user_dict), 200)
            else:
                return make_response(jsonify(message="User not found"), 404)
        except Exception as e:
            return make_response(jsonify(message="Error updating user"), 500)


@app.route('/admin/transactions', methods=['GET'])
def view_transactions():
    try:
        transactions = Transaction.query.all()
        transactions_list = [transaction.to_dict() for transaction in transactions]
        return make_response(jsonify(transactions_list), 200)
    except Exception as e:
        return make_response(jsonify(message="Error retrieving transactions"), 500)

@app.route('/admin/wallet-analytics', methods=['GET'])
def view_wallet_analytics_admin():
    try:
       
        wallet_accounts = WalletAccount.query.all()
        total_balance = sum([wallet.balance for wallet in wallet_accounts])
        average_balance = total_balance / len(wallet_accounts)

        analytics_data = {
            "total_balance": total_balance,
            "average_balance": average_balance,
        }

        return make_response(jsonify(analytics_data), 200)
    except Exception as e:
        return make_response(jsonify(message="Error retrieving wallet analytics"), 500)

@app.route('/admin/profit-trends', methods=['GET'])
def view_profit_trends():
    try:
        
        profit_transactions = Transaction.query.filter(Transaction.amount > 0).all()
        profit_transactions_list = [transaction.to_dict() for transaction in profit_transactions]

        return make_response(jsonify(profit_transactions_list), 200)
    except Exception as e:
        return make_response(jsonify(message="Error retrieving profit trends"), 500)
    





@app.route('/dashboard', methods=['GET'])
@jwt_required()
def get_dashboard_data():
    try:
        current_user_id = get_jwt_identity()

        print(f'Current User ID: {current_user_id}')  

        user = User.query.get(current_user_id)

        if user:
            return jsonify({
                'user': {
                    'username': user.username,
                    'email': user.email,
                },
                'message': 'User data retrieved successfully'
            }), 200
        else:
            print('User not found in the database') 
            return jsonify({'message': 'User not found'}), 404

    except Exception as e:
        app.logger.error(f'Error fetching user data: {str(e)}')
        return jsonify({'message': 'Internal Server Error'}), 500

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
