def teacherEntity(teacher) -> dict:
    return {
        "id": str(teacher["_id"]),
        "username": teacher["username"],
        "password": teacher["password"],
        "email": teacher["email"],
        "phone": teacher["phone"],
        "students": [str(student) for student in teacher["students"]],
        "address": teacher["address"]
    }

def teacherEntityList(teachers) -> list:
    return [teacherEntity(teacher) for teacher in teachers]
