"""FastAPI routers for security endpoints.

Endpoints:
- POST /api/security/encrypt: encrypt a string.
- POST /api/security/decrypt: decrypt a token.
- POST /api/security/scan: upload a file for malware scan.
- GET /api/security/events: retrieve logged events.
"""

from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse

from ..models import SecurityEvent
from ..security import encrypt_data, decrypt_data, scan_file, log_event, EVENT_LOG

router = APIRouter()

@router.post("/encrypt")
async def encrypt_endpoint(data: dict):
    plain_text = data.get("text")
    if not plain_text:
        raise HTTPException(status_code=400, detail="'text' field required")
    token = encrypt_data(plain_text)
    log_event(user_id=1, event_type="ENCRYPT", description="Encrypted data")
    return JSONResponse(content={"token": token})

@router.post("/decrypt")
async def decrypt_endpoint(data: dict):
    token = data.get("token")
    if not token:
        raise HTTPException(status_code=400, detail="'token' field required")
    try:
        plain_text = decrypt_data(token)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid token")
    log_event(user_id=1, event_type="DECRYPT", description="Decrypted data")
    return JSONResponse(content={"text": plain_text})

@router.post("/scan")
async def scan_endpoint(file: UploadFile = File(...)):
    file_bytes = await file.read()
    clean = scan_file(file_bytes)
    log_event(user_id=1, event_type="SCAN", description=f"Scanned file {file.filename}")
    return JSONResponse(content={"clean": clean})

@router.get("/events")
async def get_events():
    return JSONResponse(content=EVENT_LOG)
