import datetime
import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config.config import ALGORITHM, SECRET
from config.db import redis_client

JWT_SECRET = SECRET
JWT_ALGORITHM = ALGORITHM


def token_response(token: str):
    return {
        "access_token": token
    }


async def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    
    #await redis_client.set(user_id, token, 600)

    return token_response(token)

async def renewJWT(decoded_token: dict):
    try:
        if redis_client.ttl(decoded_token["user_id"]) <= 60 or decoded_token["exp"] <= datetime.timedelta(minutes=1):
            return await signJWT(decoded_token["user_id"])
    except:
        return None


async def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        # futura parte do if para verificar token em cache: redis_client.ttl(decoded_token["user_id"]) > 0 or
        #https://github.com/frontendbr/forum/discussions/1471
        if decoded_token["exp"] >= datetime.datetime.utcnow():
              return decoded_token
        else: 
            return None
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
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid token")
    
    def verify_jwt(self, jwt_token: str):
        is_token_valid : bool = False

        payload = decodeJWT(jwt_token)

        print(payload)

        if payload:
            is_token_valid = True
        return is_token_valid
    