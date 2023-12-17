from sqlalchemy_serializer import SerializerMixin;
from models.base import db
from sqlalchemy import Numeric



class Wallet_account(db.Model, SerializerMixin):
    __tablename__ = "wallet_accounts"
    
    
    id= db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    balance = db.Column(Numeric(precision=10, scale=2), nullable=False)
    
    
    def __repr__(self):
        return f'<Wallet_account {self.user_id}: {self.balance}>'