from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, database
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    userId: str
    password: str
    remember: bool = False

@router.post("/login")
def login(login_req: LoginRequest, db: Session = Depends(database.get_db)):
    user = crud.get_user_by_userid(db, login_req.userId)
    if not user or login_req.password != "password":
        raise HTTPException(status_code=400, detail="Invalid credentials supplied")
    return {
        "token": "dummy-token",
        "user": user
    }
