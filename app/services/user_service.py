from app import db, make_response
from app.models.user import User


class UserService:
       def get_user():
           
            users = []
            for user in User.query.all():
                user_dict = user.to_dict()
                users.append(user_dict)

            response = make_response(
                users,
                200)

            return response 
    
def get_user_id(user_id):
           
            users = []
            for user in User.query.filter(user_id).first():
                user_dict = user.to_dict()
                users.append(user_dict)

            response = make_response(
                users,
            200
        )

            return response
        
def create_user():
            users = User(
                username = 'username',
                password = 'password',
                fullname = 'fullname',
                email = 'email',
                address = 'address',
                digital_signature = 'digital_signature'
            )
            
            db.session.add(users)
            db.session.commit()
        
            response = make_response(
                users.to_dict(),
            201
        )
            return response
            
            
            
def delete_user(user_id):
    
    users = User.query.get(user_id)
    db.session.delete(users)
    db.session.commit 
    
    response = make_response(
            users,
            200
        )

    return response, {"message":"Deleted Successfully"}    
    
    
    
    
    
    
    
    