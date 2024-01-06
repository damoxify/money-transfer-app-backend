from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Beneficiary(db.Model, SerializerMixin):
    __tablename__ = "beneficiaries"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    account_number = db.Column(db.Integer)
    bank = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    transactions = db.relationship('Transaction', backref='beneficiary')
