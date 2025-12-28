"""
Text Encryption Page - CLEAN DESIGN FOR ALL ALGORITHMS
"""
import streamlit as st
from text_encryption import (
    transposition_encrypt, transposition_decrypt,
    caesar_encrypt, caesar_decrypt,
    affine_encrypt, affine_decrypt,
    hill_encrypt, hill_decrypt, is_valid_hill_key,
    vigenere_encrypt, vigenere_decrypt,
    des_encrypt, des_decrypt,
    aes_encrypt, aes_decrypt,
    rsa_encrypt, rsa_decrypt, rsa_generate_keys
)

# Clean, minimal CSS
st.markdown("""
<style>
    /* Clean container styling */
    .section-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 4px solid #007bff;
    }
    
    .result-container {
        background-color: #e9f7ef;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #d4edda;
        margin: 10px 0;
        font-family: 'Courier New', monospace;
    }
    
    .matrix-container {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #cce5ff;
        margin: 10px 0;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #0056b3;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    
    /* Header styling */
    .section-title {
        color: #2c3e50;
        border-bottom: 2px solid #eaeaea;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    /* Info box */
    .info-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 0 5px 5px 0;
    }
    
    /* Success/Error messages */
    .success-msg {
        color: #155724;
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
    }
    
    .error-msg {
        color: #721c24;
        background-color: #f8d7da;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔐 Text Encryption")
st.markdown("Select an encryption algorithm from the dropdown below.")
st.markdown("---")

# Algorithm selection
algorithms = {
    "Transposition Cipher": {"icon": "🔀", "desc": "Rearrange characters"},
    "Caesar Cipher": {"icon": "🔢", "desc": "Shift letters"},
    "Affine Cipher": {"icon": "📐", "desc": "Mathematical encryption"},
    "Hill Cipher": {"icon": "🧮", "desc": "Matrix encryption"},
    "Vigenere Cipher": {"icon": "🔠", "desc": "Keyword encryption"},
    "DES (Simplified)": {"icon": "🔐", "desc": "Block cipher"},
    "AES (Simplified)": {"icon": "🔒", "desc": "Advanced encryption"},
    "RSA (Simplified)": {"icon": "🔑", "desc": "Public-key encryption"}
}

selected_algo = st.selectbox(
    "**Select Algorithm:**",
    list(algorithms.keys()),
    help=f"Currently selected: {algorithms[selected_algo]['desc'] if 'selected_algo' in locals() else 'Choose an algorithm'}"
)

# Show algorithm description
st.markdown(f"**{algorithms[selected_algo]['icon']} {selected_algo}** - {algorithms[selected_algo]['desc']}")
st.markdown("---")

# Create two columns for encryption/decryption
col1, col2 = st.columns([1, 1])

# ============================================
# HILL CIPHER - Clean Design
# ============================================
if selected_algo == "Hill Cipher":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        
        # Text input
        input_text = st.text_area("**Plain Text:**", height=120,
                                 placeholder="Enter text to encrypt...")
        
        if input_text:
            clean_text = ''.join([c for c in input_text.upper() if c.isalpha()])
            st.caption(f"Alphabetic characters: {len(clean_text)}")
        
        # Matrix configuration
        st.markdown("---")
        st.markdown("#### Key Matrix Configuration")
        
        # Matrix size
        matrix_size = st.radio("Matrix Size:", ["2×2", "3×3"], horizontal=True)
        n = 2 if matrix_size == "2×2" else 3
        
        # Matrix input
        st.markdown('<div class="matrix-container">', unsafe_allow_html=True)
        if n == 2:
            st.markdown("**Enter 2×2 Matrix Values (0-25):**")
            col_a, col_b = st.columns(2)
            with col_a:
                a11 = st.number_input("a₁₁", 0, 25, 6, key="hill_enc_a11")
                a21 = st.number_input("a₂₁", 0, 25, 24, key="hill_enc_a21")
            with col_b:
                a12 = st.number_input("a₁₂", 0, 25, 13, key="hill_enc_a12")
                a22 = st.number_input("a₂₂", 0, 25, 16, key="hill_enc_a22")
            key_matrix = [[a11, a12], [a21, a22]]
        else:
            st.markdown("**Enter 3×3 Matrix Values (0-25):**")
            cols = st.columns(3)
            with cols[0]:
                a11 = st.number_input("a₁₁", 0, 25, 6, key="hill3_a11")
                a21 = st.number_input("a₂₁", 0, 25, 24, key="hill3_a21")
                a31 = st.number_input("a₃₁", 0, 25, 1, key="hill3_a31")
            with cols[1]:
                a12 = st.number_input("a₁₂", 0, 25, 13, key="hill3_a12")
                a22 = st.number_input("a₂₂", 0, 25, 16, key="hill3_a22")
                a32 = st.number_input("a₃₂", 0, 25, 3, key="hill3_a32")
            with cols[2]:
                a13 = st.number_input("a₁₃", 0, 25, 20, key="hill3_a13")
                a23 = st.number_input("a₂₃", 0, 25, 17, key="hill3_a23")
                a33 = st.number_input("a₃₃", 0, 25, 8, key="hill3_a33")
            key_matrix = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]
        
        # Matrix validation
        if is_valid_hill_key(key_matrix):
            st.markdown('<div class="success-msg">✓ Valid matrix</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error-msg">✗ Invalid matrix determinant</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close matrix-container
        
        # Encrypt button
        if st.button("**Encrypt**", key="enc_hill", use_container_width=True):
            if input_text:
                if is_valid_hill_key(key_matrix):
                    with st.spinner("Encrypting..."):
                        encrypted = hill_encrypt(input_text, key_matrix)
                        st.session_state.hill_encrypted = encrypted
                        st.markdown("**Encrypted Text:**")
                        st.code(encrypted)
                else:
                    st.error("Please use a valid matrix.")
            else:
                st.warning("Please enter text to encrypt.")
        
        st.markdown('</div>', unsafe_allow_html=True)  # Close section-container
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        
        # Cipher text input
        cipher_text = st.text_area("**Cipher Text:**", height=120,
                                  placeholder="Enter text to decrypt...",
                                  key="dec_hill_cipher")
        
        # Show encrypted text if available
        if 'hill_encrypted' in st.session_state:
            with st.expander("**Last Encrypted Text:**", expanded=False):
                st.code(st.session_state.hill_encrypted)
        
        # Decrypt button
        if st.button("**Decrypt**", key="dec_hill", use_container_width=True):
            if cipher_text:
                if is_valid_hill_key(key_matrix):
                    with st.spinner("Decrypting..."):
                        decrypted = hill_decrypt(cipher_text, key_matrix)
                        if "Error:" in decrypted:
                            st.error(decrypted)
                        else:
                            st.markdown("**Decrypted Text:**")
                            st.code(decrypted)
                else:
                    st.error("Invalid matrix for decryption.")
            else:
                st.warning("Please enter cipher text.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# TRANSPOSITION CIPHER - Clean Design
# ============================================
elif selected_algo == "Transposition Cipher":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        key = st.text_input("**Key:**", "KEY")
        
        if st.button("**Encrypt**", key="enc_trans"):
            if input_text:
                encrypted = transposition_encrypt(input_text, key)
                st.markdown("**Encrypted Text:**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_text = st.text_area("**Cipher Text:**", height=120, key="dec_trans_cipher")
        key = st.text_input("**Key:**", "KEY", key="dec_trans_key")
        
        if st.button("**Decrypt**", key="dec_trans"):
            if cipher_text:
                decrypted = transposition_decrypt(cipher_text, key)
                st.markdown("**Decrypted Text:**")
                st.code(decrypted)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# CAESAR CIPHER - Clean Design
# ============================================
elif selected_algo == "Caesar Cipher":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        shift = st.slider("**Shift Value:**", 0, 25, 3)
        
        if st.button("**Encrypt**", key="enc_caesar"):
            if input_text:
                encrypted = caesar_encrypt(input_text, shift)
                st.markdown("**Encrypted Text:**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_text = st.text_area("**Cipher Text:**", height=120, key="dec_caesar_cipher")
        shift = st.slider("**Shift Value:**", 0, 25, 3, key="dec_caesar_shift")
        
        if st.button("**Decrypt**", key="dec_caesar"):
            if cipher_text:
                decrypted = caesar_decrypt(cipher_text, shift)
                st.markdown("**Decrypted Text:**")
                st.code(decrypted)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# AFFINE CIPHER - Clean Design
# ============================================
elif selected_algo == "Affine Cipher":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        col_a, col_b = st.columns(2)
        with col_a:
            a = st.number_input("**a value:**", 1, 25, 5, 
                               help="Must be coprime with 26")
        with col_b:
            b = st.number_input("**b value:**", 0, 25, 8)
        
        if st.button("**Encrypt**", key="enc_affine"):
            if input_text:
                encrypted = affine_encrypt(input_text, a, b)
                st.markdown("**Encrypted Text:**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_text = st.text_area("**Cipher Text:**", height=120, key="dec_affine_cipher")
        col_a, col_b = st.columns(2)
        with col_a:
            a = st.number_input("**a value:**", 1, 25, 5, key="dec_affine_a")
        with col_b:
            b = st.number_input("**b value:**", 0, 25, 8, key="dec_affine_b")
        
        if st.button("**Decrypt**", key="dec_affine"):
            if cipher_text:
                decrypted = affine_decrypt(cipher_text, a, b)
                st.markdown("**Decrypted Text:**")
                st.code(decrypted)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# VIGENERE CIPHER - Clean Design
# ============================================
elif selected_algo == "Vigenere Cipher":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        key = st.text_input("**Key:**", "SECRET")
        
        if st.button("**Encrypt**", key="enc_vigenere"):
            if input_text:
                encrypted = vigenere_encrypt(input_text, key)
                st.markdown("**Encrypted Text:**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_text = st.text_area("**Cipher Text:**", height=120, key="dec_vigenere_cipher")
        key = st.text_input("**Key:**", "SECRET", key="dec_vigenere_key")
        
        if st.button("**Decrypt**", key="dec_vigenere"):
            if cipher_text:
                decrypted = vigenere_decrypt(cipher_text, key)
                st.markdown("**Decrypted Text:**")
                st.code(decrypted)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# DES (SIMPLIFIED) - Clean Design
# ============================================
elif selected_algo == "DES (Simplified)":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        key = st.text_input("**Key (8 characters):**", "DESKEY12")
        
        if st.button("**Encrypt**", key="enc_des"):
            if input_text:
                encrypted = des_encrypt(input_text, key)
                st.markdown("**Encrypted Text:**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_text = st.text_area("**Cipher Text:**", height=120, key="dec_des_cipher")
        key = st.text_input("**Key (8 characters):**", "DESKEY12", key="dec_des_key")
        
        if st.button("**Decrypt**", key="dec_des"):
            if cipher_text:
                decrypted = des_decrypt(cipher_text, key)
                st.markdown("**Decrypted Text:**")
                st.code(decrypted)
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# AES (SIMPLIFIED) - Clean Design
# ============================================
elif selected_algo == "AES (Simplified)":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        key = st.text_input("**Key:**", "AESKEY1234567890")
        
        if st.button("**Encrypt**", key="enc_aes"):
            if input_text:
                encrypted = aes_encrypt(input_text, key)
                st.markdown("**Encrypted Text (Hex):**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_hex = st.text_area("**Cipher Text (Hex):**", height=120, key="dec_aes_cipher")
        key = st.text_input("**Key:**", "AESKEY1234567890", key="dec_aes_key")
        
        if st.button("**Decrypt**", key="dec_aes"):
            if cipher_hex:
                try:
                    decrypted = aes_decrypt(cipher_hex, key)
                    st.markdown("**Decrypted Text:**")
                    st.code(decrypted)
                except:
                    st.error("Invalid cipher text format. Please enter valid hexadecimal.")
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# RSA (SIMPLIFIED) - Clean Design
# ============================================
elif selected_algo == "RSA (Simplified)":
    
    with col1:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Encryption")
        input_text = st.text_area("**Plain Text:**", height=120)
        
        # Generate keys if not exists
        if 'rsa_keys' not in st.session_state:
            st.session_state.rsa_keys = rsa_generate_keys()
        
        public_key, private_key = st.session_state.rsa_keys
        
        st.markdown(f"**Public Key:** `{public_key}`")
        st.markdown(f"**Private Key:** `{private_key}`")
        
        if st.button("**Encrypt**", key="enc_rsa"):
            if input_text:
                encrypted = rsa_encrypt(input_text, public_key)
                st.markdown("**Encrypted Text:**")
                st.code(encrypted)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown("### Decryption")
        cipher_text = st.text_area("**Cipher Text (comma-separated):**", 
                                  height=120, key="dec_rsa_cipher",
                                  placeholder="Enter numbers separated by commas...")
        
        if 'rsa_keys' in st.session_state:
            _, private_key = st.session_state.rsa_keys
            
            if st.button("**Decrypt**", key="dec_rsa"):
                if cipher_text:
                    try:
                        decrypted = rsa_decrypt(cipher_text, private_key)
                        st.markdown("**Decrypted Text:**")
                        st.code(decrypted)
                    except:
                        st.error("Invalid cipher text format. Please enter comma-separated numbers.")
        st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# ALGORITHM INFORMATION SECTION
# ============================================
st.markdown("---")
with st.expander(f"📖 About {selected_algo}", expanded=True):
    
    if selected_algo == "Transposition Cipher":
        st.markdown("""
        **Transposition Cipher** rearranges the positions of characters without changing the characters themselves.
        
        **How it works:**
        1. Write the text in rows of a fixed length (determined by the key)
        2. Rearrange columns according to the alphabetical order of the key
        3. Read columns in the new order to create cipher text
        
        **Example:** Key "KEY" (alphabetical order: E=1, K=2, Y=3)
        """)
        
    elif selected_algo == "Caesar Cipher":
        st.markdown("""
        **Caesar Cipher** is one of the simplest substitution ciphers.
        
        **How it works:**
        1. Each letter is shifted a fixed number of positions down the alphabet
        2. The shift value serves as the key
        3. Decryption uses the same shift in reverse
        
        **Example:** Shift = 3
        - A → D, B → E, C → F, ..., X → A, Y → B, Z → C
        """)
        
    elif selected_algo == "Affine Cipher":
        st.markdown("""
        **Affine Cipher** is a monoalphabetic substitution cipher using a mathematical function.
        
        **Encryption Formula:** E(x) = (ax + b) mod 26
        
        **Requirements:**
        - 'a' must be coprime with 26 (gcd(a, 26) = 1)
        - 'b' can be any integer from 0 to 25
        
        **Decryption Formula:** D(x) = a⁻¹(x - b) mod 26
        where a⁻¹ is the modular multiplicative inverse of a modulo 26
        """)
        
    elif selected_algo == "Hill Cipher":
        st.markdown("""
        **Hill Cipher** is a polygraphic substitution cipher based on linear algebra.
        
        **How it works:**
        1. Text is converted to numbers (A=0, B=1, ..., Z=25)
        2. Text is divided into blocks of size n
        3. Each block is multiplied by an n×n key matrix
        4. Results are taken modulo 26
        5. Convert back to letters
        
        **Matrix Requirements:**
        - Must be square (n×n)
        - Determinant must be coprime with 26
        - For decryption, the inverse matrix modulo 26 is needed
        
        **Example (2×2):** 
        \\[ C = K \\times P \\mod 26 \\]
        \\[ P = K^{-1} \\times C \\mod 26 \\]
        """)
        
    elif selected_algo == "Vigenere Cipher":
        st.markdown("""
        **Vigenere Cipher** is a polyalphabetic substitution cipher.
        
        **How it works:**
        1. A keyword is repeated to match the length of the plaintext
        2. Each letter is shifted according to the corresponding keyword letter
        3. Different Caesar shifts are used for different positions
        
        **Advantages over Caesar Cipher:**
        - More secure due to multiple shift values
        - Resists frequency analysis better
        """)
        
    elif selected_algo == "DES (Simplified)":
        st.markdown("""
        **DES (Data Encryption Standard)** is a symmetric-key block cipher.
        
        **Note:** This is a simplified educational version.
        
        **Original DES Features:**
        - 64-bit block size
        - 56-bit key length
        - 16 rounds of encryption
        - Uses Feistel network structure
        
        **This Implementation:**
        - Simplified XOR-based encryption
        - For educational purposes only
        """)
        
    elif selected_algo == "AES (Simplified)":
        st.markdown("""
        **AES (Advanced Encryption Standard)** is a symmetric encryption algorithm.
        
        **Note:** This is a simplified educational version.
        
        **Original AES Features:**
        - 128-bit block size
        - Key sizes: 128, 192, or 256 bits
        - Multiple rounds (10, 12, or 14)
        - Uses substitution-permutation network
        
        **This Implementation:**
        - Simplified XOR encryption with SHA-256 key hash
        - For educational purposes only
        """)
        
    elif selected_algo == "RSA (Simplified)":
        st.markdown("""
        **RSA (Rivest-Shamir-Adleman)** is a public-key cryptosystem.
        
        **Note:** This implementation uses small primes for demonstration.
        
        **How RSA Works:**
        1. Choose two prime numbers p and q
        2. Compute n = p × q and φ(n) = (p-1)(q-1)
        3. Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
        4. Compute d such that d × e ≡ 1 mod φ(n)
        
        **Public Key:** (e, n)
        **Private Key:** (d, n)
        
        **Encryption:** c = mᵉ mod n
        **Decryption:** m = cᵈ mod n
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding-top: 20px;">
<hr>
Developed by Amine EL HANINE<br>
<small>Multi-Algorithm Encryption Suite © 2025</small>
</div>
""", unsafe_allow_html=True)