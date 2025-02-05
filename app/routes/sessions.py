from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, database

router = APIRouter()

def fake_auth(token: str = "dummy-token"):
    if token != "dummy-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token

@router.get("")
def get_sessions(startDate: str = None, endDate: str = None, db: Session = Depends(database.get_db), token: str = Depends(fake_auth)):
    sessions = crud.get_sessions(db, userId="user123", startDate=startDate, endDate=endDate)
    return sessions

@router.post("")
def create_session(data: dict, db: Session = Depends(database.get_db), token: str = Depends(fake_auth)):
    location = data.get("location")
    if not location:
        raise HTTPException(status_code=400, detail="Location is required")
    session = crud.create_session(db, userId="user123", location=location)
    return session

@router.post("/{sessionId}/clock-out")
def clock_out(sessionId: str, data: dict, db: Session = Depends(database.get_db), token: str = Depends(fake_auth)):
    location = data.get("location")
    if not location:
        raise HTTPException(status_code=400, detail="Location is required")
    session = crud.update_session_clock_out(db, sessionId, location)
    if not session:
        raise HTTPException(status_code=400, detail="Invalid sessionId")
    return session
