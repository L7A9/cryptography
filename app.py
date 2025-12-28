"""
Main Streamlit Application
"""
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Multi-Algorithm Encryption Suite",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("Multi-Algorithm Encryption Suite")
    st.markdown("---")
    
    # Welcome message
    st.markdown("""
    ## Welcome to the Encryption Suite!
    
    This application provides multiple encryption algorithms for both text and images.
    
    ### Navigation:
    - Use the sidebar to select different pages
    - Each page contains specific encryption algorithms
    
    ### Available Algorithms:
    
    **Text Encryption:**
    - Transposition Cipher
    - Caesar Cipher
    - Affine Cipher
    - Hill Cipher
    - Vigenere Cipher
    - DES (Simplified)
    - AES (Simplified)
    - RSA (Simplified)
    
    **Image Encryption:**
    - Chaotic Encryption using Logistic and PWLCM maps
    
    ### How to use:
    1. Select a page from the sidebar
    2. Choose an encryption algorithm
    3. Enter your text or upload an image
    4. Provide encryption key/parameters
    5. Encrypt/Decrypt as needed
    """)
    
    st.markdown("---")
    
    # Quick links
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Text Encryption**\n\nEncrypt and decrypt text using classical and modern algorithms.")
    
    with col2:
        st.warning("**Image Encryption**\n\nEncrypt images using chaotic encryption techniques.")
    
    with col3:
        st.success("**About**\n\nLearn about the algorithms and their implementations.")
    
    st.markdown("---")
    
    # Add name at the bottom
    st.markdown("""
    <div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <hr>
    Developed by [Amine EL HANINE]<br>
    Multi-Algorithm Encryption Suite © 2025
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()