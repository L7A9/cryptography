"""
Chaotic Image Encryption Implementation - FIXED VERSION
"""
import numpy as np
import hashlib

def generate_key_from_hash(key: str, shape: tuple) -> np.ndarray:
    """Generate deterministic key array from hash matching image shape"""
    # Generate SHA-256 hash from key
    key_hash = hashlib.sha256(key.encode()).digest()
    
    # Create deterministic seed from hash (ensure it's within valid range)
    # Use modulo to ensure seed is within 0 to 2^32 - 1
    seed = int.from_bytes(key_hash[:4], 'big') % (2**32 - 1)
    
    # Generate key array matching image shape
    if len(shape) == 3:
        # Color image (height, width, channels)
        height, width, channels = shape
        key_array = np.zeros((height, width, channels), dtype=np.uint8)
        # Generate key for each channel separately
        for c in range(channels):
            # Create new random state for each channel with different seed
            channel_seed = (seed + c * 1000) % (2**32 - 1)
            rng = np.random.RandomState(channel_seed)
            key_array[:, :, c] = rng.randint(0, 256, size=(height, width), dtype=np.uint8)
    else:
        # Grayscale image (height, width)
        height, width = shape
        rng = np.random.RandomState(seed)
        key_array = rng.randint(0, 256, size=(height, width), dtype=np.uint8)
    
    return key_array

def chaotic_image_encrypt(image_array: np.ndarray, key: str) -> np.ndarray:
    """Simple XOR-based image encryption that works correctly"""
    # Ensure image is uint8 and copy to avoid modifying original
    image_array = image_array.astype(np.uint8).copy()
    
    # Generate key array matching image shape
    key_array = generate_key_from_hash(key, image_array.shape)
    
    # XOR encryption
    encrypted = np.bitwise_xor(image_array, key_array)
    
    return encrypted.astype(np.uint8)

def chaotic_image_decrypt(encrypted_array: np.ndarray, key: str) -> np.ndarray:
    """Decrypt image - XOR is symmetric, so same as encryption"""
    # Ensure encrypted array is uint8
    encrypted_array = encrypted_array.astype(np.uint8).copy()
    
    # Generate same key array
    key_array = generate_key_from_hash(key, encrypted_array.shape)
    
    # XOR decryption (same as encryption for XOR)
    decrypted = np.bitwise_xor(encrypted_array, key_array)
    
    return decrypted.astype(np.uint8)

# Alternative simpler method without RandomState
def simple_xor_encrypt(image_array: np.ndarray, key: str) -> np.ndarray:
    """Even simpler XOR encryption using hash directly"""
    # Get image dimensions
    if len(image_array.shape) == 3:
        height, width, channels = image_array.shape
    else:
        height, width = image_array.shape
        channels = 1
    
    # Generate key from hash
    key_hash = hashlib.sha256(key.encode()).digest()
    key_bytes = bytearray(key_hash)
    
    # Repeat key to match image size
    total_pixels = height * width * channels
    key_expanded = bytearray()
    
    while len(key_expanded) < total_pixels:
        key_expanded.extend(key_bytes)
    
    # Trim to exact size
    key_expanded = key_expanded[:total_pixels]
    
    # Convert to numpy array
    key_array = np.frombuffer(key_expanded, dtype=np.uint8)
    
    # Reshape to match image
    if channels > 1:
        key_array = key_array.reshape(height, width, channels)
    else:
        key_array = key_array.reshape(height, width)
    
    # XOR encryption
    encrypted = np.bitwise_xor(image_array, key_array)
    
    return encrypted.astype(np.uint8)

def simple_xor_decrypt(encrypted_array: np.ndarray, key: str) -> np.ndarray:
    """Decrypt using simple XOR method"""
    return simple_xor_encrypt(encrypted_array, key)