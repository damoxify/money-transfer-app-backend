from flask import Flask

class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # Add a secret key for securing sessions and CSRF protection
    SECRET_KEY = 'your_secret_key'

    # Configuration for JWT (JSON Web Tokens) authentication
    JWT_SECRET_KEY = 'your_jwt_secret_key'
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
    
    # Define the SQLAlchemy Database URI
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/your_database'

    # Add other configurations as needed
    SWAGGER_PATH = 'swagger.yaml'
