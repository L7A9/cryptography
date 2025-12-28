"""
Transposition Cipher Implementation
"""
import math

def transposition_encrypt(text: str, key: str) -> str:
    """Transposition cipher encryption"""
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    key_len = len(key)
    
    # Create empty matrix
    num_rows = math.ceil(len(text) / key_len)
    matrix = [['' for _ in range(key_len)] for _ in range(num_rows)]
    
    # Fill matrix with text
    idx = 0
    for i in range(num_rows):
        for j in range(key_len):
            if idx < len(text):
                matrix[i][j] = text[idx]
                idx += 1
    
    # Get column order based on key
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    
    # Read columns in key order
    cipher_text = ''
    for col in key_order:
        for row in range(num_rows):
            cipher_text += matrix[row][col]
    
    return cipher_text

def transposition_decrypt(cipher: str, key: str) -> str:
    """Transposition cipher decryption"""
    key_len = len(key)
    num_rows = math.ceil(len(cipher) / key_len)
    
    # Get column order
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    inverse_order = [0] * len(key_order)
    for i, pos in enumerate(key_order):
        inverse_order[pos] = i
    
    # Create empty matrix
    matrix = [['' for _ in range(key_len)] for _ in range(num_rows)]
    
    # Fill matrix column by column
    idx = 0
    for col in range(key_len):
        actual_col = inverse_order[col]
        for row in range(num_rows):
            if idx < len(cipher):
                matrix[row][actual_col] = cipher[idx]
                idx += 1
    
    # Read row by row
    plain_text = ''
    for i in range(num_rows):
        for j in range(key_len):
            plain_text += matrix[i][j]
    
    return plain_text