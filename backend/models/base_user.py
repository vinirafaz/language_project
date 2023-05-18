from pydantic import BaseModel, validator, Json, EmailStr
from typing import Optional, List


class AddressBase(BaseModel):
    street: Optional[str]
    number: Optional[int]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    zip: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "street": "Rua dos Bobos",
                "number": 0,
                "city": "São Paulo",
                "state": "SP",
                "country": "Brasil",
                "zip": "00000-000"
            }
        }


class BaseUser(BaseModel):
    id: Optional[str]
    username: str
    email: EmailStr
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "email": "teste@teste.com",
    #             "username": "admin"
    #         }
    #     }    




class BaseUserInDb(BaseUser):
    password: str
    

class BaseUserLogged(BaseUserInDb):
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[Json[AddressBase]]
    languages: List[str]
    is_customer: bool    