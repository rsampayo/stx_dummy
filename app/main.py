from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import auth, sessions, geofences, checklist
from app.seed import seed_data

# Create tables and seed data
Base.metadata.create_all(bind=engine)
seed_data()

app = FastAPI(title="STX dummy server")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
app.include_router(geofences.router, prefix="/geofences", tags=["geofences"])
app.include_router(checklist.router, prefix="/checklist", tags=["checklist"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
