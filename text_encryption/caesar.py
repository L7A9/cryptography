"""
Caesar Cipher Implementation
"""
def caesar_encrypt(text: str, shift: int) -> str:
    """Caesar cipher encryption"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(cipher: str, shift: int) -> str:
    """Caesar cipher decryption"""
    return caesar_encrypt(cipher, -shift)