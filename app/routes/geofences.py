from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, database

router = APIRouter()

def fake_auth(token: str = "dummy-token"):
    if token != "dummy-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token

@router.get("")
def get_geofences(db: Session = Depends(database.get_db), token: str = Depends(fake_auth)):
    geofences = crud.get_geofences(db)
    return geofences
