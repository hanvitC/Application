from fastapi import Depends, FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app.routers import courses, user_router, notes_router, study_sessions_router

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(courses.router)
app.include_router(user_router.router)
app.include_router(notes_router.router)
app.include_router(study_sessions_router.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
