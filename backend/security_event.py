# security_event.py
from datetime import datetime
from pydantic import BaseModel

class SecurityEvent(BaseModel):
    user_id: str
    event_type: str
    description: str
    timestamp: datetime = datetime.utcnow()
