def noteEntity(note) -> dict:
    return {
        "id": str(note["_id"]),
        "date": note["date"],
        "themes": [str(theme) for theme in note["themes"]],
        "new_words": [str(card_id) for card_id in note["new_words"]],
        "pronunciation": [dict(pronunciation) for pronunciation in note["pronunciation"]],
        "rocked_when_said": [str(rocked) for rocked in note["rocked_when_i_say"]],
        "review": [str(review) for review in note["review"]]
    }

def noteEntityList(notes) -> list:
    return [noteEntity(note) for note in notes]