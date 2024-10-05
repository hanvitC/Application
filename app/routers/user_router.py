from fastapi import APIRouter

from app.models.user import User
from app.resources.user_resource import UserResource
from app.services.service_factory import ServiceFactory

router = APIRouter()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.resources.user_resource import UserResource

router = APIRouter()


# Dependency for the UserResource service
def get_user_service():
    return UserResource(config=None)


# Get a user by ID
@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int) -> User:
    res = ServiceFactory.get_service("UserResource")
    result = res.get_by_key(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result



# Create a new user
@router.post("/users", tags=["users"])
async def create_user(user_data: dict, user_service: UserResource = Depends(get_user_service)):
    user_service.create_user(user_data)
    return {"message": "User created successfully"}


# Delete a user by ID
@router.delete("/users/{user_id}", tags=["users"])
async def delete_user(user_id: int, user_service: UserResource = Depends(get_user_service)):
    user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}

