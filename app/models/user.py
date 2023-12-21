from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    fullname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    digital_signature = db.Column(db.String(255))
    
    wallet_accounts = db.relationship('WalletAccount', backref="user", cascade='all, delete-orphan')
    beneficiaries = db.relationship('Beneficiary', backref="user", cascade='all, delete-orphan')
    transactions = db.relationship('Transaction', secondary='beneficiaries', back_populates=('users'))
    
    def __repr__(self):
        return f'<User {self.username}: {self.fullname}, {self.email}>'
