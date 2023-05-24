from config.db import connection
from bson import ObjectId

async def find_one_note(note_id):
    response = connection.teste.note.find_one({"_id": ObjectId(note_id)})
    return response


async def create_one_note(object):
    return str(connection.teste.note.insert_one(object).inserted_id)


async def update_one_note(note_id, note):
    pass


async def create_one_card(object):
    return str(connection.teste.cards.insert_one(object).inserted_id)

