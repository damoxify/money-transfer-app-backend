from flask import Blueprint, jsonify, request
from models.transaction import Transaction  
from models.user import User 

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/transactions', methods=['GET'])
def list_all_transactions():
    try:
        transactions = Transaction.query.all()

        response = {
            'transactions': [{'id': transaction.id, 'amount': transaction.amount} for transaction in transactions],
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/users', methods=['GET'])
def list_all_users():
    try:
        users = User.query.all()

        response = {
            'users': [{'id': user.id, 'username': user.username} for user in users],
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
