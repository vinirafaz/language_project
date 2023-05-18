from fastapi import APIRouter, Depends
from controllers.auth_control import jwtBearer

notes = APIRouter()

@notes.get("/notes", dependencies=[Depends(jwtBearer())])
async def get_notes():
    return {"message": "Notes from database"}


@notes.get("/notes/{note_id}", dependencies=[Depends(jwtBearer())])
async def get_note_by_id(note_id: int):
    return {"message": f"Note with id {note_id}"}


@notes.post("/notes")
async def create_note():
    pass
