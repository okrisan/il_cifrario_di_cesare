from base64 import b64decode

def base64_decode(text: str | bytes) -> bytes:
    return b64decode(text)