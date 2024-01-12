from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Numeric, MetaData
import datetime
import jwt
from flask import current_app

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Beneficiary(db.Model, SerializerMixin):
    __tablename__ = "beneficiaries"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    account_number = db.Column(db.Integer)
    bank = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User', back_populates='beneficiaries')
    transactions = db.relationship('Transaction', back_populates='beneficiary')

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'
        
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(Numeric(precision=10, scale=2), nullable=False)
    narration = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    beneficiary_id = db.Column(db.Integer, db.ForeignKey('beneficiaries.id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    status = db.Column(db.String)

    user = db.relationship('User', back_populates='transactions')
    beneficiary = db.relationship('Beneficiary', back_populates='transactions')

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    digital_signature = db.Column(db.String(255))
    admin = db.Column(db.Boolean, nullable=False, default=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    is_authenticated = db.Column(db.Boolean, default=False)
    
    wallet_accounts = db.relationship('WalletAccount', backref="user", cascade='all, delete-orphan')
    beneficiaries = db.relationship('Beneficiary', back_populates='user', cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', secondary='beneficiaries', back_populates='user')
    
    def __repr__(self):
        return f'<User {self.username}: {self.fullname}, {self.email}>'

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

class WalletAccount(db.Model, SerializerMixin):
    __tablename__ = "wallet_accounts"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    balance = db.Column(Numeric(precision=10, scale=2), nullable=False)
    
    def __repr__(self):
        return f'<WalletAccount {self.user_id}: {self.balance}>'
