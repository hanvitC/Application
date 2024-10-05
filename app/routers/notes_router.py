from fastapi import APIRouter, Depends, HTTPException
from app.resources.notes_resource import NotesResource

router = APIRouter()


# Dependency for the NotesResource service
def get_notes_service():
    return NotesResource()


# Get notes by user_id
@router.get("/users/{user_id}/notes", tags=["notes"])
async def get_notes(user_id: int, notes_service: NotesResource = Depends(get_notes_service)):
    result = notes_service.get_by_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="No notes found for this user")
    return result


# Create a new note
@router.post("/notes", tags=["notes"])
async def create_note(note_data: dict, notes_service: NotesResource = Depends(get_notes_service)):
    notes_service.create_note(note_data)
    return {"message": "Note created successfully"}


# Delete a note by ID
@router.delete("/notes/{note_id}", tags=["notes"])
async def delete_note(note_id: int, notes_service: NotesResource = Depends(get_notes_service)):
    notes_service.delete_note(note_id)
    return {"message": "Note deleted successfully"}
