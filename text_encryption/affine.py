"""
Affine Cipher Implementation
"""
from utils import mod_inverse

def affine_encrypt(text: str, a: int, b: int) -> str:
    """Affine cipher encryption: E(x) = (ax + b) mod 26"""
    result = ""
    for char in text:
        if char.isupper():
            x = ord(char) - 65
            result += chr((a * x + b) % 26 + 65)
        elif char.islower():
            x = ord(char) - 97
            result += chr((a * x + b) % 26 + 97)
        else:
            result += char
    return result

def affine_decrypt(cipher: str, a: int, b: int) -> str:
    """Affine cipher decryption: D(x) = a^-1(x - b) mod 26"""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "Error: 'a' must be coprime with 26"
    
    result = ""
    for char in cipher:
        if char.isupper():
            x = ord(char) - 65
            result += chr((a_inv * (x - b)) % 26 + 65)
        elif char.islower():
            x = ord(char) - 97
            result += chr((a_inv * (x - b)) % 26 + 97)
        else:
            result += char
    return result