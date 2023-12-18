from flask_restx import Namespace, Resource
from flask import current_app, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix  

swagger_namespace = Namespace('swagger', description='Swagger Documentation')


@swagger_namespace.route('/')
class SwaggerResource(Resource):
    def get(self):
        """
        Get Swagger UI
        """
        swagger_path = current_app.config.get('app.swagger', 'swagger.json')

        with open(swagger_path) as f:
            data = f.read()

        return jsonify(data)
