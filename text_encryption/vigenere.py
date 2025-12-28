"""
Vigenere Cipher Implementation
"""
def vigenere_encrypt(text: str, key: str) -> str:
    """Vigenere cipher encryption"""
    key = key.upper()
    key_len = len(key)
    result = ""
    
    for i, char in enumerate(text):
        if char.isupper():
            shift = ord(key[i % key_len]) - 65
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            shift = ord(key[i % key_len].lower()) - 97
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def vigenere_decrypt(cipher: str, key: str) -> str:
    """Vigenere cipher decryption"""
    key = key.upper()
    key_len = len(key)
    result = ""
    
    for i, char in enumerate(cipher):
        if char.isupper():
            shift = ord(key[i % key_len]) - 65
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            shift = ord(key[i % key_len].lower()) - 97
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char
    
    return result