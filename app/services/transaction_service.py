from app import db
from app.models.transaction import Transaction
from wallet_service import WalletService

class TransactionService:
    @staticmethod
    def create_transaction(sender_wallet_id, recipient_wallet_id, amount):
        new_transaction = Transaction(sender_wallet_id=sender_wallet_id, recipient_wallet_id=recipient_wallet_id, amount=amount)
        db.session.add(new_transaction)
        db.session.commit()
        return new_transaction

    @staticmethod
    def get_transactions_by_user(user_id):
   
        user_wallet = WalletService.get_wallet_by_user_id(user_id)
        if user_wallet:
            return Transaction.query.filter((Transaction.sender_wallet_id == user_wallet.id) | (Transaction.recipient_wallet_id == user_wallet.id)).all()
        return []

