from app import db
from app.models.wallet import Wallet

class WalletService:
    @staticmethod
    def create_wallet(user_id):

        try:
            if not user_id:
                raise ValueError("Invalid user_id for creating a wallet")

            new_wallet = Wallet(user_id=user_id)
            db.session.add(new_wallet)
            db.session.commit()

            return new_wallet

        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_wallet_by_user_id(user_id):
 
        try:
            if not user_id:
                raise ValueError("Invalid user_id for retrieving a wallet")

            return Wallet.query.filter_by(user_id=user_id).first()

        except Exception as e:
            raise e
