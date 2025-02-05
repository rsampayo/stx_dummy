from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Location(BaseModel):
    latitude: float
    longitude: float

class User(BaseModel):
    id: str
    userId: str
    name: str
    role: str
    createdAt: datetime

    class Config:
        orm_mode = True

class Session(BaseModel):
    id: str
    userId: str
    clockIn: datetime
    clockOut: Optional[datetime] = None
    location: Location
    status: str

    class Config:
        orm_mode = True

class Geofence(BaseModel):
    id: str
    name: str
    type: str
    center: Optional[Location] = None
    radius: Optional[float] = None
    polygon: Optional[List[Location]] = None

    class Config:
        orm_mode = True

class ChecklistItem(BaseModel):
    id: str
    label: str
    inputType: str

class ChecklistSection(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    applicableFor: List[str]
    items: List[ChecklistItem]

class ChecklistTemplate(BaseModel):
    id: str
    name: str
    description: str
    sections: List[ChecklistSection]

    class Config:
        orm_mode = True

class ChecklistItemResponse(BaseModel):
    itemId: str
    answer: str

class ChecklistResponseSection(BaseModel):
    sectionId: str
    itemResponses: List[ChecklistItemResponse]

class ChecklistSubmission(BaseModel):
    templateId: str
    sessionId: Optional[str] = None
    phase: str
    responses: List[ChecklistResponseSection]

class Error(BaseModel):
    code: int
    message: str
