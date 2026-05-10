"""Core security logic: encryption, malware scanning, and event logging.

- Encryption: AES-256 GCM using Fernet.
- Malware scan: placeholder that checks a file against a simple signature list.
- Event logger: writes events to an in‑memory list (replace with DB in prod).
"""

import base64
import os
from datetime import datetime
from typing import List

from cryptography.fernet import Fernet

# Generate or load a symmetric key (in production store securely)
KEY_FILE = os.path.join(os.path.dirname(__file__), "secret.key")
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
else:
    with open(KEY_FILE, "rb") as f:
        key = f.read()

fernet = Fernet(key)

# In‑memory event store (replace with DB or message broker)
EVENT_LOG: List[dict] = []

# Simple malware signature list (hashes of known bad files)
MALWARE_SIGNATURES = {
    "d41d8cd98f00b204e9800998ecf8427e",  # example SHA-256 of empty file
}


def encrypt_data(plain_text: str) -> str:
    """Encrypt plain text using Fernet (AES‑256 GCM)."""
    token = fernet.encrypt(plain_text.encode("utf-8"))
    return token.decode("utf-8")


def decrypt_data(token: str) -> str:
    """Decrypt token back to plain text."""
    plain = fernet.decrypt(token.encode("utf-8"))
    return plain.decode("utf-8")


def scan_file(file_bytes: bytes) -> bool:
    """Scan file bytes against known malware signatures.

    Returns True if file is clean, False if malware detected.
    """
    import hashlib
    sha256 = hashlib.sha256(file_bytes).hexdigest()
    if sha256 in MALWARE_SIGNATURES:
        return False
    return True


def log_event(user_id: int, event_type: str, description: str = "") -> None:
    """Append a security event to the in‑memory log."""
    event = {
        "id": len(EVENT_LOG) + 1,
        "user_id": user_id,
        "event_type": event_type,
        "description": description,
        "timestamp": datetime.utcnow().isoformat(),
    }
    EVENT_LOG.append(event)

# Expose public API
__all__ = [
    "encrypt_data",
    "decrypt_data",
    "scan_file",
    "log_event",
    "EVENT_LOG",
]
