def userEntity(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "username": user["username"],
        "password": user["password"],
        "email": user["email"],
        "teacher": [str(teachers_id) for teachers_id in user["teachers"]],
        "notes": [str(note_id) for note_id in user["notes"]]
    }

def userEntityList(users) -> list:

    teste = [userEntity(user) for user in users]
    return teste
