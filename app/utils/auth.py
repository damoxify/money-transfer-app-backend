from flask import current_app, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from app.models.user import User

def generate_token(user_id, expiration=3600):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': user_id}).decode('utf-8')

def verify_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        user = User.query.get(data['id'])
        g.current_user = user 
        return True
    except (BadSignature, SignatureExpired):
        return False
