from db.queries import find_one_note, create_one_note, create_one_card, update_one_note
from integrations.ia_translation import translation
from models.notes import NoteBase
from fastapi import HTTPException
from models.schemas.note import noteEntity, noteEntityList
from bson import ObjectId


async def get_note_by_id(note_id: str):
    try:
        return noteEntity(await find_one_note(note_id))
    except Exception:
        raise HTTPException(status_code=404, detail="Note not found")



async def create_note_object(note: dict):
    try:
        return await create_one_note(note)
    except Exception:
        raise HTTPException(status_code=500, detail="Error creating note")
    

async def create_card_object(words: list):

    object_list = []

    try:
        for word in words:
            print("ENTROU NO FOR " + word)
            translated = await translation(word)
            card = {
                "in_portuguese": word,
                "in_english": translated,''
                "rating": 5
            }
        
            id = await create_one_card(card)

            object_list.append(ObjectId(id))
        return object_list
    except Exception:
        raise HTTPException(status_code=500, detail="Error creating card")


async def chang_note_by_id(note_id: str, note: NoteBase):
    try:

        new_note = note.dict()



        return await update_one_note(note_id, new_note)
    except Exception:
        raise HTTPException(status_code=500, detail="Error updating note")