# README.md
# Mobile Security App

## Overview
This repository contains a minimal but functional mobile security backend (FastAPI) and frontend (Vue3) implementation. It demonstrates core security features such as data encryption, event logging, and a simple UI to view security events.

## Backend
- **FastAPI** with in‑memory storage (replace with a DB for production).
- Endpoints for user management, event logging, and encryption/decryption.
- Uses **cryptography.Fernet** for symmetric encryption.

## Frontend
- **Vue3** + **Vite**.
- Simple dashboard showing security events fetched from the backend.
- Axios proxy configured to forward `/api` requests to the FastAPI server.

## Running
```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd ../frontend
npm install
npm run dev
```

## Security Notes
- In production, store encryption keys securely (e.g., HSM, KMS).
- Replace in‑memory storage with a persistent DB and add authentication.
- Add rate limiting, input validation, and logging.
