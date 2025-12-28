"""
Simplified AES Implementation (Educational)
"""
import hashlib

def aes_encrypt(text: str, key: str) -> str:
    """Simplified AES encryption (educational version)"""
    # Generate key schedule
    key_hash = hashlib.sha256(key.encode()).digest()
    
    # Simple XOR with key hash
    result_bytes = []
    for i, char in enumerate(text):
        key_byte = key_hash[i % len(key_hash)]
        result_bytes.append(ord(char) ^ key_byte)
    
    # Convert to hex string
    return ''.join(format(b, '02x') for b in result_bytes)

def aes_decrypt(cipher_hex: str, key: str) -> str:
    """Simplified AES decryption"""
    # Convert hex to bytes
    cipher_bytes = bytes.fromhex(cipher_hex)
    
    # Generate key hash
    key_hash = hashlib.sha256(key.encode()).digest()
    
    # Decrypt
    result = ""
    for i, byte in enumerate(cipher_bytes):
        key_byte = key_hash[i % len(key_hash)]
        result += chr(byte ^ key_byte)
    
    return result