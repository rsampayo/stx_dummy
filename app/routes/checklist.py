from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, database

router = APIRouter()

def fake_auth(token: str = "dummy-token"):
    if token != "dummy-token":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token

@router.get("/template")
def get_checklist_template(db: Session = Depends(database.get_db), token: str = Depends(fake_auth)):
    template = crud.get_checklist_template(db)
    if not template:
        raise HTTPException(status_code=404, detail="Checklist template not found")
    return template

@router.post("/submission")
def submit_checklist(data: dict, db: Session = Depends(database.get_db), token: str = Depends(fake_auth)):
    return {"message": "Checklist submitted successfully."}
