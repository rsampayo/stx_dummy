import uuid
from sqlalchemy import Column, String, DateTime, Float, JSON
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    userId = Column(String, unique=True, index=True)
    name = Column(String)
    role = Column(String)
    createdAt = Column(DateTime, server_default=func.now())

class Session(Base):
    __tablename__ = "sessions"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    userId = Column(String, index=True)
    clockIn = Column(DateTime, server_default=func.now())
    clockOut = Column(DateTime, nullable=True)
    location = Column(JSON)
    status = Column(String, default="active")

class Geofence(Base):
    __tablename__ = "geofences"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)  # circle or polygon
    center = Column(JSON, nullable=True)
    radius = Column(Float, nullable=True)
    polygon = Column(JSON, nullable=True)

class ChecklistTemplate(Base):
    __tablename__ = "checklist_templates"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    sections = Column(JSON)
