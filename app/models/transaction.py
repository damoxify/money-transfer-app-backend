from sqlalchemy_serializer import SerializerMixin;
from base import db;

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'
    
    id =db.Column(db.Integer, primary_key= True)
    amount= db.Column(db.Decimal, nullable=False)
    narration=db.Column(db.String)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    beneficiary_id =db.Column(db.Integer, db.ForeignKey('beneficiaries.id'))
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    status= db.Column(db.String)
    

    def __repr__(self):
        return f'<Transaction {self.id}: {self.amount}, {self.user_id}>'