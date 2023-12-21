from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Numeric

db = SQLAlchemy()

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'
        
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(Numeric(precision=10, scale=2), nullable=False)
    narration = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    beneficiary_id = db.Column(db.Integer, db.ForeignKey('beneficiaries.id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    status = db.Column(db.String)
    
    def __repr__(self):
        return f'<Transaction {self.id}: {self.amount}, {self.user_id}>'
