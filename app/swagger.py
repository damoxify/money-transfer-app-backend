# app/swagger.py
from flask_restx import Api, Namespace, Resource, fields
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from flask import jsonify, current_app

api = Api()

# Define input models
user_input_model = api.model('UserInput', {
    'username': fields.String(required=True),
    'password': fields.String(required=True),
    'fullname': fields.String(required=True),
    'email': fields.String(required=True),
    'address': fields.String(),
    'digital_signature': fields.String(),
})

beneficiary_input_model = api.model('BeneficiaryInput', {
    'name': fields.String(required=True),
    'account_number': fields.Integer(required=True),
    'bank': fields.String(required=True),
    'user_id': fields.Integer(required=True),
})

transaction_input_model = api.model('TransactionInput', {
    'amount': fields.Float(required=True),
    'narration': fields.String(),
    'user_id': fields.Integer(required=True),
    'beneficiary_id': fields.Integer(required=True),
    'status': fields.String(),
})

wallet_account_input_model = api.model('WalletAccountInput', {
    'user_id': fields.Integer(required=True),
    'balance': fields.Float(required=True),
})

swagger_namespace = Namespace('swagger', description='Swagger Documentation')

@api.route('/swagger')
class SwaggerResource(MethodResource):
    @marshal_with(None)
    @doc(description='Get Swagger UI', security=[{"BearerAuth": []}])
    def get(self):
        swagger_path = current_app.config.get('app.swagger', 'swagger.json')

        with open(swagger_path) as f:
            data = f.read()

        return jsonify(data)

api.add_namespace(swagger_namespace)
# app/swagger.py
from flask_restx import Api, Namespace, Resource, fields
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from flask import jsonify, current_app

api = Api()

# Define input models
user_input_model = api.model('UserInput', {
    'username': fields.String(required=True),
    'password': fields.String(required=True),
    'fullname': fields.String(required=True),
    'email': fields.String(required=True),
    'address': fields.String(),
    'digital_signature': fields.String(),
})

beneficiary_input_model = api.model('BeneficiaryInput', {
    'name': fields.String(required=True),
    'account_number': fields.Integer(required=True),
    'bank': fields.String(required=True),
    'user_id': fields.Integer(required=True),
})

transaction_input_model = api.model('TransactionInput', {
    'amount': fields.Float(required=True),
    'narration': fields.String(),
    'user_id': fields.Integer(required=True),
    'beneficiary_id': fields.Integer(required=True),
    'status': fields.String(),
})

wallet_account_input_model = api.model('WalletAccountInput', {
    'user_id': fields.Integer(required=True),
    'balance': fields.Float(required=True),
})

swagger_namespace = Namespace('swagger', description='Swagger Documentation')

@api.route('/swagger')
class SwaggerResource(MethodResource):
    @marshal_with(None)
    @doc(description='Get Swagger UI', security=[{"BearerAuth": []}])
    def get(self):
        swagger_path = current_app.config.get('app.swagger', 'swagger.json')

        with open(swagger_path) as f:
            data = f.read()

        return jsonify(data)

api.add_namespace(swagger_namespace)
