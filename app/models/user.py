
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "email": "testuser@example.com",
                "last_name": "Doe",
                "first_name": "John"
            }
        }
