"""
FastAPI router for security related endpoints.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List

from ..security import encrypt_data, decrypt_data, simple_malware_check
from ..models import User, SecurityEvent, Vulnerability
from ..config import settings

router = APIRouter()

class EncryptRequest(BaseModel):
    data: str

class EncryptResponse(BaseModel):
    token: str

class DecryptRequest(BaseModel):
    token: str

class DecryptResponse(BaseModel):
    data: str

class MalwareCheckRequest(BaseModel):
    data: str

class MalwareCheckResponse(BaseModel):
    is_malicious: bool
    reason: str

@router.post("/encrypt", response_model=EncryptResponse)
async def encrypt_endpoint(req: EncryptRequest):
    token = encrypt_data(req.data)
    return EncryptResponse(token=token)

@router.post("/decrypt", response_model=DecryptResponse)
async def decrypt_endpoint(req: DecryptRequest):
    try:
        data = decrypt_data(req.token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
    return DecryptResponse(data=data)

@router.post("/malware-check", response_model=MalwareCheckResponse)
async def malware_check_endpoint(req: MalwareCheckRequest):
    is_malicious, reason = simple_malware_check(req.data)
    return MalwareCheckResponse(is_malicious=is_malicious, reason=reason)
