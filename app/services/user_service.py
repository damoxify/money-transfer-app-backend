from app import db, make_response
from app.models.user import User

class UserService:
    @staticmethod
    def get_all_users():
        try:
            users = User.query.all()
            user_list = [user.to_dict() for user in users]

            response = make_response(user_list, 200)
            return response

        except Exception as e:
            raise e

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = User.query.get(user_id)

            if user:
                user_dict = user.to_dict()
                response = make_response(user_dict, 200)
                return response
            else:
                return make_response({"message": "User not found"}, 404)

        except Exception as e:
            raise e

    @staticmethod
    def create_user():
        try:
            new_user = User(
                username='username',
                password='password',
                fullname='fullname',
                email='email',
                address='address',
                digital_signature='digital_signature'
            )

            db.session.add(new_user)
            db.session.commit()

            response = make_response(new_user.to_dict(), 201)
            return response

        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)

            if user:
                db.session.delete(user)
                db.session.commit()

                response = make_response(user.to_dict(), 200)
                return response, {"message": "Deleted Successfully"}
            else:
                return make_response({"message": "User not found"}, 404)

        except Exception as e:
            raise e
