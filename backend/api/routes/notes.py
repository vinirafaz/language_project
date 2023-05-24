from fastapi import APIRouter, Depends
from controllers.auth_control import jwtBearer
from models.notes import NoteBase
import controllers.notes_controller as nc


notes = APIRouter()

@notes.get("/notes", tags=['notes'])
async def get_notes():
    return {"message": "Notes from database"}


@notes.get("/notes/{note_id}", tags=['notes'])
async def get_note_by_id(note_id: str):
    return await nc.get_note_by_id(note_id)


@notes.post("/notes", tags=['notes'])
async def create_note(note: NoteBase):
    new_note = dict(note)
    del new_note["id"]
    id_words = await nc.create_card_object(new_note["new_words"])

    new_note["new_words"] = new_note["new_words"].clear()
    new_note["new_words"] = id_words


    return await nc.create_note_object(new_note)
    
