"""
FastAPI application entry point for the Mobile Security App backend.

This module sets up the FastAPI app, includes routers, and configures
middleware for logging and security.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import security
from .config import settings

app = FastAPI(
    title=settings.app_name,
    description="Backend API for Mobile Security App",
    version="0.1.0",
)

# CORS configuration – allow all origins for demo purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(security.router, prefix="/api/security", tags=["security"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
