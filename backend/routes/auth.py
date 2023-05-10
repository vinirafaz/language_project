from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config.config import ALGORITHM, SECRET
import datetime
import jwt


JWT_SECRET = SECRET
JWT_ALGORITHM = ALGORITHM

# Auxiliary Function

def token_response(token: str):
    return {
        "access_token": token
    }


def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["exp"] >= datetime.datetime.utcnow() else None
    except:
        return None
    

class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_error)


    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme")
            else:
                raise HTTPException(status_code=403, detail="Invalid token")
    
    def verify_jwt(self, jwt_token: str):
        is_token_valid : bool = False
        payload = decodeJWT(jwt_token)

        if payload:
            is_token_valid = True
        return is_token_valid