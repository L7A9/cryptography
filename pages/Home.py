"""
Home Page
"""
import streamlit as st

st.title("🏠 Home")
st.markdown("---")

st.markdown("""
## Multi-Algorithm Encryption Suite

This application provides a comprehensive collection of encryption algorithms 
for educational and demonstration purposes.

### Features:

#### 📝 Text Encryption Algorithms:
1. **Classical Ciphers:**
   - Transposition Cipher
   - Caesar Cipher
   - Affine Cipher
   - Hill Cipher
   - Vigenere Cipher

2. **Modern Ciphers (Simplified):**
   - DES (Data Encryption Standard)
   - AES (Advanced Encryption Standard)
   - RSA (Public Key Cryptography)

#### 🖼️ Image Encryption Algorithms:
1. **Chaotic Image Encryption:**
   - Based on Logistic Map and PWLCM
   - Combines substitution and permutation
   - High security with chaotic sequences

### Educational Purpose:
This application is designed for:
- Learning about different encryption techniques
- Understanding algorithm implementations
- Visualizing encryption processes
- Comparing different encryption methods

### How to Use:
1. Navigate to the desired page using the sidebar
2. Select an encryption algorithm
3. Follow the instructions for each algorithm
4. Experiment with different keys and parameters

### Security Note:
⚠️ **Important:** This application is for educational purposes only. 
The simplified implementations are not suitable for real-world security applications.
""")

# Add name at the bottom
st.markdown("""
    <div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <hr>
    Developed by [Amine EL HANINE]<br>
    Multi-Algorithm Encryption Suite © 2025
    </div>
            """, unsafe_allow_html=True)