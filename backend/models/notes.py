from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from bson import ObjectId

class NoteBase(BaseModel):
    id: Optional[str]
    date: datetime = datetime.now()
    themes: Optional[list]
    new_words: Optional[list]
    pronunciation: Optional[list[dict]]
    rocked_when_i_say: Optional[list]
    review: Optional[list]        
    
    class Config:
        schema_extra = {
            "example": {
                "themes": ["theme1", "theme2"],
                "new_words": ["word1", "word2"],
                "pronunciation": [ { "Iron" : "/ˈaɪrn/" }, { "Robot" : "/ˈrəʊbət/" } ],
                "rocked_when_i_say": ["word1", "word2"],    
                "review": ["word1", "word2"]
            }
        }



class Cards(BaseModel):
    id: Optional[str]
    in_portuguese: Optional[str]
    in_english: Optional[str]
    rating: Optional[int]