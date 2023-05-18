from models.base_user import BaseUserLogged
from typing import Optional

class Customer(BaseUserLogged):
    teachers: Optional[list[str]] = []
    notes: Optional[list[str]] = []
    