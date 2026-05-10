"""Pydantic models for the mobile security domain.

- User: represents an authenticated user.
- SecurityEvent: logs runtime events (e.g., suspicious activity).
- Vulnerability: stores known vulnerability signatures.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class SecurityEvent(BaseModel):
    id: int
    user_id: int
    event_type: str
    description: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Vulnerability(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    severity: str  # e.g., LOW, MEDIUM, HIGH, CRITICAL
    discovered_at: datetime = Field(default_factory=datetime.utcnow)
