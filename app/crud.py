from sqlalchemy.orm import Session
from app import models, schemas
import uuid
from datetime import datetime

def get_user_by_userid(db: Session, userId: str):
    return db.query(models.User).filter(models.User.userId == userId).first()

def create_user(db: Session, user: schemas.User):
    db_user = models.User(
        id=user.id if user.id else str(uuid.uuid4()),
        userId=user.userId,
        name=user.name,
        role=user.role,
        createdAt=user.createdAt if user.createdAt else datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_session(db: Session, userId: str, location: dict):
    db_session = models.Session(
        userId=userId,
        clockIn=datetime.utcnow(),
        location=location,
        status="active"
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def get_sessions(db: Session, userId: str, startDate: str = None, endDate: str = None):
    query = db.query(models.Session).filter(models.Session.userId == userId)
    return query.all()

def update_session_clock_out(db: Session, session_id: str, location: dict):
    db_session = db.query(models.Session).filter(models.Session.id == session_id).first()
    if db_session:
        db_session.clockOut = datetime.utcnow()
        db_session.location = location
        db_session.status = "completed"
        db.commit()
        db.refresh(db_session)
    return db_session

def get_geofences(db: Session):
    return db.query(models.Geofence).all()

def get_checklist_template(db: Session):
    return db.query(models.ChecklistTemplate).first()
