from jose import jwt
from app.config import SECRET_KEY, ALGORITHM

def create_token(user):
    return jwt.encode({"user": user}, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])