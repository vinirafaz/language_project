from fastapi import APIRouter, Depends
from routes.auth import jwtBearer

notes = APIRouter()

@notes.get("/api/v1/notes", dependencies=[Depends(jwtBearer())])
def get_notes():
    return {"message": "Notes from database"}


@notes.get("/api/v1/notes/{note_id}")
def get_note_by_id(note_id: int):
    return {"message": f"Note with id {note_id}"}

@notes.post("/api/v1/notes")
def create_note():
    pass
