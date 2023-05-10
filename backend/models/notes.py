from pydantic import BaseModel
from typing import Optional
import datetime

class NoteBase(BaseModel):
    id: Optional[str]
    date: datetime = datetime.now()
    themes: Optional[list]
    new_words: Optional[list]
    pronunciation: Optional[list]
    rocked_when_i_say: Optional[list]
    review: Optional[list]