from flask import Blueprint, jsonify, request
from flask_restx import Namespace, Resource
from app.pagination.pagination import Pagination
from app.models.user import User

user_bp = Blueprint('user', __name__)
user_ns = Namespace('user', description='User operations')
pagination = Pagination()

@user_ns.route('/list', methods=['GET'])
class ListUsers(Resource):
    def get(self):
        try:
            page = request.args.get('page', default=1, type=int)
            per_page = request.args.get('per_page', default=10, type=int)

            users_query = User.query

            paginated_users = pagination.paginate_query(users_query, page, per_page)

            response = {
                'users': [{'id': user.id, 'username': user.username} for user in paginated_users['items']],
                'pagination': {
                    'page': paginated_users['page'],
                    'total_pages': paginated_users['total_pages'],
                    'total_items': paginated_users['total_items'],
                }
            }

            return jsonify(response), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
