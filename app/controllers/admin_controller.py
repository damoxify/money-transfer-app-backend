from flask import Blueprint, jsonify
from flask_restx import Namespace, Resource
from app.models.transaction import Transaction  
from app.models.user import User

admin_bp = Blueprint('admin', __name__)

admin_ns = Namespace('admin', description='Admin operations')

@admin_ns.route('/transactions', methods=['GET'])
class ListAllTransactions(Resource):
    def get(self):
        try:
            transactions = Transaction.query.all()

            response = {
                'transactions': [{'id': transaction.id, 'amount': transaction.amount} for transaction in transactions],
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500

@admin_ns.route('/users', methods=['GET'])
class ListAllUsers(Resource):
    def get(self):
        try:
            users = User.query.all()

            response = {
                'users': [{'id': user.id, 'username': user.username} for user in users],
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
