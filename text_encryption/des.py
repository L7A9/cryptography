"""
Simplified DES Implementation (Educational)
"""
from .caesar import caesar_encrypt, caesar_decrypt

def des_encrypt(text: str, key: str) -> str:
    """Simplified DES encryption (educational version)"""
    # Convert key to binary
    key_bin = ''.join(format(ord(c), '08b') for c in key[:8])
    if len(key_bin) > 64:
        key_bin = key_bin[:64]
    
    # Simple XOR encryption
    result = ""
    for i, char in enumerate(text):
        key_char = key_bin[i % len(key_bin)]
        shift = int(key_char)
        result += caesar_encrypt(char, shift)
    
    return result

def des_decrypt(cipher: str, key: str) -> str:
    """Simplified DES decryption"""
    key_bin = ''.join(format(ord(c), '08b') for c in key[:8])
    if len(key_bin) > 64:
        key_bin = key_bin[:64]
    
    result = ""
    for i, char in enumerate(cipher):
        key_char = key_bin[i % len(key_bin)]
        shift = int(key_char)
        result += caesar_decrypt(char, shift)
    
    return result