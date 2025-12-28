"""
Simplified RSA Implementation (Educational)
"""
import math
from utils import mod_inverse

def rsa_generate_keys():
    """Generate RSA keys (simplified)"""
    # Small primes for demonstration
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e
    e = 17
    while math.gcd(e, phi) != 1:
        e += 1
    
    # Calculate d
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def rsa_encrypt(text: str, public_key: tuple) -> str:
    """RSA encryption"""
    e, n = public_key
    encrypted = []
    
    for char in text:
        m = ord(char)
        c = pow(m, e, n)
        encrypted.append(str(c))
    
    return ','.join(encrypted)

def rsa_decrypt(cipher: str, private_key: tuple) -> str:
    """RSA decryption"""
    d, n = private_key
    encrypted_nums = [int(x) for x in cipher.split(',')]
    
    result = ""
    for c in encrypted_nums:
        m = pow(c, d, n)
        result += chr(m)
    
    return result