"""
Core security logic: encryption/decryption and simple malware check.
"""

import base64
from cryptography.fernet import Fernet
from typing import Tuple

# In a real system the key would be stored securely
FERNET_KEY = Fernet.generate_key()
fernet = Fernet(FERNET_KEY)


def encrypt_data(plain_text: str) -> str:
    """Encrypt plain text using Fernet symmetric encryption."""
    token = fernet.encrypt(plain_text.encode("utf-8"))
    return token.decode("utf-8")


def decrypt_data(token: str) -> str:
    """Decrypt token back to plain text."""
    plain = fernet.decrypt(token.encode("utf-8"))
    return plain.decode("utf-8")


def simple_malware_check(data: str) -> Tuple[bool, str]:
    """Very naive malware check – looks for suspicious patterns.
    Returns (is_malicious, reason)."""
    suspicious_patterns = ["<script>", "eval(", "exec("]
    for pat in suspicious_patterns:
        if pat.lower() in data.lower():
            return True, f"Suspicious pattern detected: {pat}"
    return False, "clean"
