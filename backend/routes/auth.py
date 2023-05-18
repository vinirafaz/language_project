from fastapi import  HTTPException, APIRouter
from controllers.auth_control import signJWT
from models.customers import Customer


auth = APIRouter()

@auth.post("/login", tags=["auth"])
async def login(username: str, password: str):
    if username == "admin" and password== "admin":
        return await signJWT(username)
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@auth.post("/register", tags=["auth"])
async def register(user: Customer):
    new_user = dict(user)

    del new_user["id"]


    return user