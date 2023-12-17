from sqlalchemy_serializer import SerializerMixin;
from models.base import db 


class Beneficiary(db.Model, SerializerMixin):
    __tablename__ = "beneficiaries"
    
    
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    account_number= db.Column(db.Integer)
    bank= db.Column(db.String)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    
    
    transactions= db.relationship('Transaction', backref='beneficiary')
    
    