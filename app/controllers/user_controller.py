from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource
from pagination.pagination import Pagination
from models.user import User
from models.transaction import Transaction

user_bp = Blueprint('user', __name__)
user_ns = Namespace('user', description='User operations')
pagination = Pagination()


@user_ns.route('/profile/<int:user_id>', methods=['GET'])
class UserProfile(Resource):
    def get(self, user_id):
        try:
            user = User.query.get(user_id)

            if user:
                response = {
                    'fullname': user.fullname,
                    'date_of_birth': user.date_of_birth,
                    'gender': user.gender,
                    'bvn': user.bvn,
                    'phone': user.phone,
                    'address': user.address,
                    'email': user.email 
                }
                return jsonify(response), 200
            else:
                return jsonify({'error': 'User not found'}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500


@user_ns.route('/transactions/<int:user_id>', methods=['GET'])
class UserTransactions(Resource):
    def get(self, user_id):
        try:
            user = User.query.get(user_id)

            if user:
                transactions_query = Transaction.query.filter_by(user_id=user.id)

                paginated_transactions = pagination.paginate_query(transactions_query, 1, 10)

                response = {
                    'transactions': [{'id': transaction.id, 'amount': transaction.amount} for transaction in paginated_transactions['items']],
                    'pagination': {
                        'page': paginated_transactions['page'],
                        'total_pages': paginated_transactions['total_pages'],
                        'total_items': paginated_transactions['total_items'],
                    }
                }
                return jsonify(response), 200
            else:
                return jsonify({'error': 'User not found'}), 404

        except Exception as e:
            return jsonify({'error': str(e)}), 500