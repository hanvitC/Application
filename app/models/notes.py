
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
class Notes(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    title: Optional[str] = None
    created_date: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "title": "Study Plan",
                "created_date": "2024-10-04T10:00:00Z"
            }
        }
