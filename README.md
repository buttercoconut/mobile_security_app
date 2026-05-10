# Mobile Security App Backend

## Overview
This repository contains a minimal FastAPI backend for a mobile security application. It demonstrates core security features such as data encryption/decryption, a naive malware check, and basic data models for users, security events, and vulnerabilities.

## Directory Structure
```
backend/
├─ Dockerfile
├─ docker-compose.yml
├─ main.py
├─ config.py
├─ models.py
├─ security.py
├─ routers/
│  └─ security.py
├─ requirements.txt
```

## Running the Service
```bash
# Build and start the container
docker compose up --build

# The API will be available at http://localhost:8000
```

## API Endpoints
- `GET /health` – Health check
- `POST /api/security/encrypt` – Encrypt data
- `POST /api/security/decrypt` – Decrypt token
- `POST /api/security/malware-check` – Check data for suspicious patterns

## Notes
- The encryption key is generated at runtime for demo purposes. In production, store it securely.
- The malware check is intentionally simple and should be replaced with a proper scanning engine.
- SQLite is used for simplicity; replace with PostgreSQL/MySQL for production.

---

Happy hacking!