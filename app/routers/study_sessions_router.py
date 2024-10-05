from fastapi import APIRouter, Depends, HTTPException
from app.resources.study_sessions_resource import StudySessionsResource

router = APIRouter()


# Dependency for the StudySessionsResource service
def get_study_sessions_service():
    return StudySessionsResource()


# Get study sessions by user_id
@router.get("/users/{user_id}/study_sessions", tags=["study_sessions"])
async def get_study_sessions(user_id: int,
                             study_sessions_service: StudySessionsResource = Depends(get_study_sessions_service)):
    result = study_sessions_service.get_by_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="No study sessions found for this user")
    return result


# Create a new study session
@router.post("/study_sessions", tags=["study_sessions"])
async def create_study_session(session_data: dict,
                               study_sessions_service: StudySessionsResource = Depends(get_study_sessions_service)):
    study_sessions_service.create_session(session_data)
    return {"message": "Study session created successfully"}


# Delete a study session by ID
@router.delete("/study_sessions/{session_id}", tags=["study_sessions"])
async def delete_study_session(session_id: int,
                               study_sessions_service: StudySessionsResource = Depends(get_study_sessions_service)):
    study_sessions_service.delete_session(session_id)
    return {"message": "Study session deleted successfully"}
