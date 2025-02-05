from app.database import SessionLocal
from app import models
from datetime import datetime

def seed_data():
    db = SessionLocal()
    # Check if already seeded
    if db.query(models.User).first():
        db.close()
        return

    # Seed a user
    user = models.User(
        id="123e4567-e89b-12d3-a456-426614174000",
        userId="user123",
        name="John Doe",
        role="employee",
        createdAt=datetime.utcnow()
    )
    db.add(user)

    # Seed a geofence
    geofence = models.Geofence(
        id="gf-001",
        name="Main Office",
        type="circle",
        center={"latitude": 40.7128, "longitude": -74.0060},
        radius=100,
        polygon=None
    )
    db.add(geofence)

    # Seed a checklist template
    checklist_template = models.ChecklistTemplate(
        id="template-001",
        name="Daily Safety Checklist",
        description="Checklist for daily safety and operational procedures.",
        sections=[
            {
                "id": "section-001",
                "title": "Pre-Operation Safety",
                "description": "Review safety protocols before starting work.",
                "applicableFor": ["clockIn"],
                "items": [
                    {
                        "id": "item-001",
                        "label": "Are all safety guards in place?",
                        "inputType": "yesNo"
                    }
                ]
            }
        ]
    )
    db.add(checklist_template)

    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
