from sqlalchemy_serializer import SerializerMixin;
from models.base import db;


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    
    
    id=db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String, unique= True, nullable=False)
    password= db.Column(db.String, nullable=False)
    fullname= db.Column(db.String, nullable=False)
    email= db.Column(db.String, nullable=False)
    address= db.Column(db.String)
    digital_signature= db.Column(db.String)
    
    wallet_accounts= db.relationship('Wallet_account', backref="user")
    beneficiaries=  db.relationship('Beneficiary', backref="user")
    transactions= db.relationship('Transaction', secondary='beneficiaries', back_populates=('users'))
    
    
    
    def __repr__(self):
        return f'<User {self.username}: {self.fullname}, {self.email}>'
    
    # gender= db.Column(db.String)
    # date_of_birth= db.Column(db.DateTime, nullable=False)
    # bvn= db.Column(db.Integer, unique= True, nullable=False)
    # phone= db.Column(db.String)
    # country= db.Column(db.String)
    