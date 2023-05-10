from pydantic import BaseModel
from typing import Optional, Dict, List


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
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address: Optional[Dict[str, AddressBase]]
    languages: List[str]
    is_customer: bool    


class BaseUserInDb(BaseUser):
    password: str
