from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from database.db import init_db
from api.generate import router as generate_router
from api.history import router as history_router

app = FastAPI(
    title="AI Social Media Campaign Generator",
    version="1.0.0"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve generated images
app.mount("/storage", StaticFiles(directory="storage"), name="storage")

# Include API routes
app.include_router(generate_router)
app.include_router(history_router)

init_db()

@app.get("/")
async def root():
    return {
        "message": "AI Social Media Campaign Generator API is running on rest API"
    }