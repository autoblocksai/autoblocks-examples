import hashlib


def md5(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()
