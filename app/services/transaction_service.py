from app import db
from app.models.transaction import Transaction
from wallet_service import WalletService

class TransactionService:
    @staticmethod
    def create_transaction(sender_wallet_id, recipient_wallet_id, amount):
        try:
            if not sender_wallet_id or not recipient_wallet_id or amount <= 0:
                raise ValueError("Invalid input parameters for creating a transaction")

            new_transaction = Transaction(sender_wallet_id=sender_wallet_id, recipient_wallet_id=recipient_wallet_id, amount=amount)
            db.session.add(new_transaction)
            db.session.commit()

            return new_transaction

        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_transactions_by_user(user_id):
        try:
            if not user_id:
                raise ValueError("Invalid user_id for retrieving transactions")

            user_wallet = WalletService.get_wallet_by_user_id(user_id)

            if user_wallet:
                return Transaction.query.filter((Transaction.sender_wallet_id == user_wallet.id) | (Transaction.recipient_wallet_id == user_wallet.id)).all()

            return []

        except Exception as e:
            raise e
