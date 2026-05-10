"""FastAPI application entry point for Mobile Security App backend.

This module sets up the FastAPI app, includes routers, and configures middleware.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import security

app = FastAPI(title="Mobile Security App Backend")

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(security.router, prefix="/api/security", tags=["security"])

@app.get("/")
async def root():
    return {"message": "Welcome to Mobile Security App Backend"}
