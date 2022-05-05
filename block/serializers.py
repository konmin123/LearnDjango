def note_to_json(note) -> dict:
    return {
        'id': note.id,
        'title': note.title,
        'message': note.message,
        'public': note.public,
    }