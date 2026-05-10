# README for backend
# Mobile Security App Backend

## Overview
This FastAPI backend provides core security services for the Mobile Security App:
- Data encryption/decryption (AES‑256 GCM via Fernet)
- Simple malware scanning against a signature list
- In‑memory event logging (replace with a DB in production)

## Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

## API Endpoints
- `POST /api/security/encrypt` – encrypt a string
- `POST /api/security/decrypt` – decrypt a token
- `POST /api/security/scan` – upload a file for malware scan
- `GET /api/security/events` – retrieve logged events

## Docker
```bash
docker build -t mobile-security-backend .
docker run -p 8000:8000 mobile-security-backend
```
