from pydantic import BaseModel, validator, Json, EmailStr
from typing import Optional, List


class AddressBase(BaseModel):
    street: Optional[str]
    number: Optional[int]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    zip: Optional[str]

class BaseUser(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr


class BaseUserInDb(BaseUser):
    password: str
    

class BaseUserLogged(BaseUserInDb):
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[Json[AddressBase]]
    languages: List[str]
    is_customer: bool    


class UserLoggin(BaseModel):
    username: str
    password: str