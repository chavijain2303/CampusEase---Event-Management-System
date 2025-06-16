from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Event
from schemas import EventCreate

router = APIRouter()

@router.post("/events/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    return {"message": "Event created successfully"}
 
