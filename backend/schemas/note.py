def noteEntity(note) -> dict:
    return {
        "id": str(note["_id"]),
        "date": note["date"],
        "themes": [str(note) for note in note["themes"]],
        "new_words": [str(note_id) for note_id in note["new_words"]],
        "pronunciation": [],
        "rocked_when_said": [],
        "review": []
    }

def noteEntityList(notes) -> list:
    return [noteEntity(note) for note in notes]