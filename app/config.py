from flask import Flask
import os

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Use a secure random key for Flask sessions and CSRF protection
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

    # Configuration for JWT (JSON Web Tokens) authentication
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'default_jwt_secret_key')
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    # Define user roles (you can extend or modify as needed)
    USER_ROLES = {
        'USER': 'User role',
        'ADMIN': 'Admin role',
    }

    # Define permissions for each role (customize based on your application needs)
    USER_PERMISSIONS = {
        'USER': ['read'],
        'ADMIN': ['read', 'write', 'admin'],
    }

    # Use environment variables for the SQLAlchemy Database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///money-transfer-app.db'

    # Add other configurations as needed
    SWAGGER_PATH = 'swagger.yaml'
