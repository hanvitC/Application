
from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class StudySessions(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "user_id": 1,
                "start_time": "2024-10-04T10:00:00Z",
                "end_time": "2024-10-04T12:00:00Z"
            }
        }
