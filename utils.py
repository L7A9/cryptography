"""
Common utility functions
"""
import hashlib
import math
from typing import List

def text_to_numbers(text: str) -> List[int]:
    """Convert text to numerical representation"""
    return [ord(char) for char in text]

def numbers_to_text(numbers: List[int]) -> str:
    """Convert numbers back to text"""
    return ''.join([chr(num) for num in numbers])

def mod_inverse(a: int, m: int) -> int:
    """Find modular inverse of a mod m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None