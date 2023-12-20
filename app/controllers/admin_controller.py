from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource
from models.transaction import Transaction
from models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

admin_bp = Blueprint('admin', __name__)

admin_ns = Namespace('admin', description='Admin operations')

@admin_ns.route('/transactions', methods=['GET'])
class ListAllTransactions(Resource):
    @jwt_required()
    def get(self):
        try:
            current_user = get_jwt_identity()
            print(f"Authenticated user: {current_user}")

            transactions = Transaction.query.all()

            response = {
                'transactions': [{'id': transaction.id, 'amount': transaction.amount} for transaction in transactions],
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

@admin_ns.route('/users', methods=['GET'])
class ListAllUsers(Resource):
    @jwt_required()  
    def get(self):
        try:
            current_user = get_jwt_identity()
            print(f"Authenticated user: {current_user}")

            users = User.query.all()

            response = {
                'users': [{'id': user.id, 'username': user.username} for user in users],
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
