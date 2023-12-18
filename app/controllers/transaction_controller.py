from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource
from pagination.pagination import Pagination
from models.transaction import Transaction

transaction_bp = Blueprint('transaction', __name__)
transaction_ns = Namespace('transaction', description='Transaction operations')
pagination = Pagination()

@transaction_ns.route('/list', methods=['GET'])
class ListTransactions(Resource):
    def get(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            transactions_query = Transaction.query

            paginated_transactions = pagination.paginate_query(transactions_query, page, per_page)

            response = {
                'transactions': [{'id': transaction.id, 'amount': transaction.amount} for transaction in paginated_transactions['items']],
                'pagination': {
                    'page': paginated_transactions['page'],
                    'total_pages': paginated_transactions['total_pages'],
                    'total_items': paginated_transactions['total_items'],
                }
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
