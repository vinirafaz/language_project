from typing import Optional
from models.base_user import BaseUser, BaseUserInDb

class TeacherBase(BaseUserInDb):
    students: Optional[list[str]] = []
    
