"""
Configuration settings for the backend.
"""

from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Mobile Security App"
    database_url: str = "sqlite:///./security.db"
    secret_key: str = "super-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()
