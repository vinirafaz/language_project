from models.base_user import BaseUser, BaseUserInDb
from typing import Optional

class Customer(BaseUserInDb):
    teachers: Optional[list[str]] = []
    notes: Optional[list[str]] = []