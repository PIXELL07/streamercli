def hash_password(password):
    return password + "_hashed"

def verify_password(password, hashed):
    return hash_password(password) == hashed