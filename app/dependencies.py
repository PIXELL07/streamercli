from fastapi import Header, HTTPException
from app.auth.jwt_handler import verify_token

def get_current_user(authorization: str = Header(None)) -> str:
    # Fixed:
    # Now reads the Authorization header and validates the JWT
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    token = authorization.split(" ")[1]
    try:
        data = verify_token(token)
        return data["user"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
