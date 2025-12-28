"""
Hill Cipher Implementation
"""
import numpy as np
from utils import mod_inverse

def mod_inverse_hill(a: int, m: int = 26) -> int:
    """Find modular inverse of a mod m"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def hill_encrypt(text: str, key_matrix: list) -> str:
    """Hill cipher encryption"""
    text = text.upper().replace(" ", "")
    # Remove non-alphabetic characters
    text_clean = ''.join([c for c in text if c.isalpha()])
    
    if len(text_clean) == 0:
        return ""
    
    n = len(key_matrix)
    
    # Pad with 'X' if needed
    if len(text_clean) % n != 0:
        text_clean += 'X' * (n - len(text_clean) % n)
    
    # Encrypt block by block
    result = ""
    for i in range(0, len(text_clean), n):
        # Convert block to vector
        vector = [ord(char) - 65 for char in text_clean[i:i+n]]
        
        # Multiply by key matrix
        encrypted_vector = [0] * n
        for row in range(n):
            for col in range(n):
                encrypted_vector[row] += key_matrix[row][col] * vector[col]
            encrypted_vector[row] %= 26
        
        # Convert back to letters
        for num in encrypted_vector:
            result += chr(num + 65)
    
    return result

def hill_decrypt(cipher: str, key_matrix: list) -> str:
    """Hill cipher decryption"""
    cipher = cipher.upper().replace(" ", "")
    cipher_clean = ''.join([c for c in cipher if c.isalpha()])
    
    if len(cipher_clean) == 0:
        return ""
    
    n = len(key_matrix)
    
    # Calculate determinant
    if n == 2:
        a, b = key_matrix[0][0], key_matrix[0][1]
        c, d = key_matrix[1][0], key_matrix[1][1]
        det = (a * d - b * c) % 26
    elif n == 3:
        a, b, c = key_matrix[0][0], key_matrix[0][1], key_matrix[0][2]
        d, e, f = key_matrix[1][0], key_matrix[1][1], key_matrix[1][2]
        g, h, i = key_matrix[2][0], key_matrix[2][1], key_matrix[2][2]
        det = (a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)) % 26
    else:
        key_np = np.array(key_matrix, dtype=np.float64)
        det = int(np.round(np.linalg.det(key_np))) % 26
    
    # Find modular inverse of determinant
    det_inv = mod_inverse_hill(det, 26)
    if det_inv is None:
        return f"Error: Matrix determinant ({det}) not invertible modulo 26"
    
    # Calculate inverse matrix for 2x2
    if n == 2:
        a, b = key_matrix[0][0], key_matrix[0][1]
        c, d = key_matrix[1][0], key_matrix[1][1]
        
        # Calculate adjugate matrix
        adj = [[d % 26, (-b) % 26],
               [(-c) % 26, a % 26]]
        
        # Multiply by modular inverse of determinant
        inv_matrix = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                inv_matrix[i][j] = (det_inv * adj[i][j]) % 26
        
        # Decrypt
        result = ""
        for i in range(0, len(cipher_clean), n):
            vector = [ord(char) - 65 for char in cipher_clean[i:i+n]]
            decrypted_vector = [0, 0]
            
            for row in range(n):
                for col in range(n):
                    decrypted_vector[row] += inv_matrix[row][col] * vector[col]
                decrypted_vector[row] %= 26
            
            for num in decrypted_vector:
                result += chr(num + 65)
        
        return result
    
    # For 3x3 or larger, use numpy
    else:
        key_np = np.array(key_matrix, dtype=np.float64)
        adj = np.round(det * np.linalg.inv(key_np)).astype(int) % 26
        inv_matrix = (det_inv * adj) % 26
        
        # Decrypt
        result = ""
        for i in range(0, len(cipher_clean), n):
            vector = [ord(char) - 65 for char in cipher_clean[i:i+n]]
            decrypted_vector = np.dot(inv_matrix, vector) % 26
            
            for num in decrypted_vector:
                result += chr(num + 65)
        
        return result

def is_valid_hill_key(key_matrix: list) -> bool:
    """Check if Hill cipher key matrix is valid"""
    n = len(key_matrix)
    if any(len(row) != n for row in key_matrix):
        return False
    
    # Calculate determinant
    if n == 2:
        a, b = key_matrix[0][0], key_matrix[0][1]
        c, d = key_matrix[1][0], key_matrix[1][1]
        det = (a * d - b * c) % 26
    else:
        key_np = np.array(key_matrix, dtype=np.float64)
        det = int(np.round(np.linalg.det(key_np))) % 26
    
    # Check if determinant is invertible modulo 26
    return mod_inverse_hill(det, 26) is not None