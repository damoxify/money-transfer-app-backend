from app import db
from app.models.wallet import Wallet_account

class WalletService:
    @staticmethod
    def create_wallet(user_id):

        new_wallet = Wallet_account(user_id=user_id)
        db.session.add(new_wallet)
        db.session.commit()
        return new_wallet

    @staticmethod
    def get_wallet_by_user_id(user_id):
    
        return Wallet_account.query.filter_by(user_id=user_id).first()

