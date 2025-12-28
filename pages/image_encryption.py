"""
Image Encryption Page - SIMPLE & RELIABLE
"""
import streamlit as st
import numpy as np
from PIL import Image
import io
from image_encryption import simple_xor_encrypt, simple_xor_decrypt

# Clean CSS
st.markdown("""
<style>
    .section-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 4px solid #28a745;
    }
    
    .image-container {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        margin: 10px 0;
    }
    
    .result-box {
        background-color: #e9f7ef;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #d4edda;
        margin: 10px 0;
    }
    
    .info-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 0 5px 5px 0;
    }
    
    .success-box {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #c3e6cb;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

st.title("🖼️ Image Encryption")
st.markdown("Encrypt and decrypt images using XOR-based encryption with SHA-256 key hashing.")
st.markdown("---")

# File uploader
st.markdown("### Upload Image")
uploaded_file = st.file_uploader(
    "Choose an image file", 
    type=['jpg', 'jpeg', 'png', 'bmp'],
    help="Upload an image to encrypt or decrypt"
)

if uploaded_file is not None:
    try:
        # Load image
        image = Image.open(uploaded_file)
        
        # Store original mode for later restoration
        original_mode = image.mode
        
        # Convert image to appropriate format
        if image.mode in ['RGBA', 'LA']:
            # Keep alpha channel
            image_array = np.array(image)
        elif image.mode == 'P':
            image = image.convert('RGB')
            image_array = np.array(image)
        elif image.mode == 'L':
            image_array = np.array(image)
        else:
            image = image.convert('RGB')
            image_array = np.array(image)
        
        # Display original image
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown("#### Original Image")
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, use_column_width=True, caption=f"Original ({original_mode})")
        
        with col2:
            st.markdown("**Image Information:**")
            st.write(f"- **Dimensions:** {image_array.shape}")
            st.write(f"- **Size:** {image.size}")
            st.write(f"- **Mode:** {original_mode}")
            st.write(f"- **Data Type:** {image_array.dtype}")
            st.write(f"- **Min/Max Values:** {image_array.min()}/{image_array.max()}")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Encryption section
        st.markdown('<div class="section-box">', unsafe_allow_html=True)
        st.markdown("#### 🔒 Encryption")
        
        enc_key = st.text_input("**Encryption Key:**", "MySecretKey123", 
                               help="Enter a secret key for encryption")
        
        if st.button("**Encrypt Image**", use_container_width=True, type="primary"):
            if enc_key:
                with st.spinner("Encrypting image..."):
                    try:
                        # Encrypt the image
                        encrypted_array = simple_xor_encrypt(image_array, enc_key)
                        
                        # Ensure values are within 0-255 range
                        encrypted_array = np.clip(encrypted_array, 0, 255).astype(np.uint8)
                        
                        # Convert to PIL Image
                        if len(encrypted_array.shape) == 3:
                            if encrypted_array.shape[2] == 4:  # RGBA
                                encrypted_image = Image.fromarray(encrypted_array, 'RGBA')
                            else:  # RGB
                                encrypted_image = Image.fromarray(encrypted_array, 'RGB')
                        else:  # Grayscale
                            encrypted_image = Image.fromarray(encrypted_array, 'L')
                        
                        # Display encrypted image
                        st.markdown("**Encrypted Image:**")
                        col_enc1, col_enc2 = st.columns(2)
                        
                        with col_enc1:
                            st.image(encrypted_image, use_column_width=True, caption="Encrypted Image")
                        
                        with col_enc2:
                            st.markdown("**Encryption Information:**")
                            st.write(f"- **Dimensions:** {encrypted_array.shape}")
                            st.write(f"- **Min/Max Values:** {encrypted_array.min()}/{encrypted_array.max()}")
                            
                            # Calculate entropy (simple measure of encryption quality)
                            unique_values = len(np.unique(encrypted_array))
                            st.write(f"- **Unique Pixel Values:** {unique_values}")
                        
                        # Save to bytes for download
                        buf = io.BytesIO()
                        encrypted_image.save(buf, format='PNG')
                        encrypted_bytes = buf.getvalue()
                        
                        # Store in session for decryption
                        st.session_state.encrypted_array = encrypted_array
                        st.session_state.encrypted_image = encrypted_image
                        st.session_state.encryption_key = enc_key
                        st.session_state.original_array = image_array
                        
                        # Download button
                        st.download_button(
                            label="**📥 Download Encrypted Image**",
                            data=encrypted_bytes,
                            file_name="encrypted_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                        
                        st.markdown('<div class="success-box">', unsafe_allow_html=True)
                        st.success("✅ Image encrypted successfully!")
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"❌ Encryption failed: {str(e)}")
            else:
                st.warning("⚠️ Please enter an encryption key.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"❌ Error loading image: {str(e)}")

# Decryption section
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("#### 🔓 Decryption")

# Option to use previously encrypted image
if 'encrypted_array' in st.session_state:
    st.markdown("**Using previously encrypted image:**")
    
    col_dec1, col_dec2 = st.columns(2)
    with col_dec1:
        st.image(st.session_state.encrypted_image, width=200, caption="Encrypted Image")
    
    dec_key = st.text_input("**Decryption Key:**", 
                           st.session_state.get('encryption_key', ''),
                           help="Enter the same key used for encryption")
    
    if st.button("**Decrypt Image**", use_container_width=True, type="secondary"):
        if dec_key:
            with st.spinner("Decrypting image..."):
                try:
                    # Decrypt the image
                    decrypted_array = simple_xor_decrypt(st.session_state.encrypted_array, dec_key)
                    
                    # Ensure values are within 0-255 range
                    decrypted_array = np.clip(decrypted_array, 0, 255).astype(np.uint8)
                    
                    # Convert to PIL Image
                    if len(decrypted_array.shape) == 3:
                        if decrypted_array.shape[2] == 4:
                            decrypted_image = Image.fromarray(decrypted_array, 'RGBA')
                        else:
                            decrypted_image = Image.fromarray(decrypted_array, 'RGB')
                    else:
                        decrypted_image = Image.fromarray(decrypted_array, 'L')
                    
                    # Display results
                    st.markdown("**Decryption Results:**")
                    col_res1, col_res2 = st.columns(2)
                    
                    with col_res1:
                        st.image(st.session_state.encrypted_image, 
                                use_column_width=True, 
                                caption="Encrypted")
                    
                    with col_res2:
                        st.image(decrypted_image, 
                                use_column_width=True, 
                                caption="Decrypted")
                    
                    # Verify decryption
                    if 'original_array' in st.session_state:
                        original_array = st.session_state.original_array.astype(np.uint8)
                        is_perfect = np.array_equal(original_array, decrypted_array)
                        
                        if is_perfect:
                            st.markdown('<div class="success-box">', unsafe_allow_html=True)
                            st.success("✅ Perfect decryption! Original image recovered exactly.")
                            st.markdown('</div>', unsafe_allow_html=True)
                        else:
                            # Calculate difference
                            diff = np.sum(np.abs(original_array.astype(int) - decrypted_array.astype(int)))
                            st.warning(f"⚠️ Decryption not perfect. Total pixel difference: {diff}")
                            
                            # Show difference (for debugging)
                            with st.expander("Show Difference Analysis"):
                                diff_percent = (diff / original_array.size) * 100
                                st.write(f"Difference percentage: {diff_percent:.6f}%")
                                
                                # Create difference visualization
                                diff_image = np.abs(original_array.astype(int) - decrypted_array.astype(int))
                                diff_image = np.clip(diff_image * 50, 0, 255).astype(np.uint8)
                                
                                if len(diff_image.shape) == 3:
                                    st.image(diff_image, caption="Difference (amplified 50x)", width=300)
                    
                    # Save decrypted image
                    buf = io.BytesIO()
                    decrypted_image.save(buf, format='PNG')
                    decrypted_bytes = buf.getvalue()
                    
                    st.download_button(
                        label="**📥 Download Decrypted Image**",
                        data=decrypted_bytes,
                        file_name="decrypted_image.png",
                        mime="image/png",
                        use_container_width=True
                    )
                    
                except Exception as e:
                    st.error(f"❌ Decryption failed: {str(e)}")
        else:
            st.warning("⚠️ Please enter the decryption key.")
else:
    st.info("👆 Encrypt an image first, then you can decrypt it here.")

st.markdown('</div>', unsafe_allow_html=True)

# Upload encrypted image option
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("#### Upload Encrypted Image")

uploaded_encrypted = st.file_uploader(
    "Or upload an encrypted image",
    type=['png', 'jpg', 'jpeg'],
    key="encrypted_upload"
)

if uploaded_encrypted:
    try:
        encrypted_img = Image.open(uploaded_encrypted)
        encrypted_arr = np.array(encrypted_img)
        
        st.markdown("**Uploaded Encrypted Image:**")
        st.image(encrypted_img, width=200)
        
        upload_dec_key = st.text_input("**Decryption Key for Uploaded Image:**", 
                                     help="Enter the key used to encrypt this image")
        
        if st.button("**Decrypt Uploaded Image**", use_container_width=True):
            if upload_dec_key:
                with st.spinner("Decrypting uploaded image..."):
                    try:
                        decrypted_array = simple_xor_decrypt(encrypted_arr, upload_dec_key)
                        decrypted_array = np.clip(decrypted_array, 0, 255).astype(np.uint8)
                        
                        # Convert to PIL Image
                        if len(decrypted_array.shape) == 3:
                            if decrypted_array.shape[2] == 4:
                                decrypted_image = Image.fromarray(decrypted_array, 'RGBA')
                            else:
                                decrypted_image = Image.fromarray(decrypted_array, 'RGB')
                        else:
                            decrypted_image = Image.fromarray(decrypted_array, 'L')
                        
                        # Display
                        col_up1, col_up2 = st.columns(2)
                        
                        with col_up1:
                            st.image(encrypted_img, use_column_width=True, caption="Uploaded Encrypted")
                        
                        with col_up2:
                            st.image(decrypted_image, use_column_width=True, caption="Decrypted")
                        
                        # Download
                        buf = io.BytesIO()
                        decrypted_image.save(buf, format='PNG')
                        decrypted_bytes = buf.getvalue()
                        
                        st.download_button(
                            label="**📥 Download Decrypted Image**",
                            data=decrypted_bytes,
                            file_name="decrypted_uploaded_image.png",
                            mime="image/png",
                            use_container_width=True
                        )
                        
                    except Exception as e:
                        st.error(f"❌ Decryption failed: {str(e)}")
            else:
                st.warning("⚠️ Please enter the decryption key.")
                
    except Exception as e:
        st.error(f"❌ Error loading encrypted image: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# Test section
st.markdown('<div class="section-box">', unsafe_allow_html=True)
st.markdown("#### 🧪 Test & Verify")

if st.button("**Run Encryption/Decryption Test**", use_container_width=True):
    # Create a simple test image
    test_image = np.zeros((100, 100, 3), dtype=np.uint8)
    
    # Draw some shapes
    test_image[30:70, 30:70] = [255, 0, 0]    # Red square
    test_image[10:20, 10:90] = [0, 255, 0]     # Green horizontal line
    test_image[80:90, 10:90] = [0, 0, 255]     # Blue horizontal line
    test_image[10:90, 45:55] = [255, 255, 0]   # Yellow vertical line
    
    test_key = "TestKey123"
    
    with st.spinner("Running test..."):
        # Encrypt
        encrypted_test = simple_xor_encrypt(test_image, test_key)
        
        # Decrypt
        decrypted_test = simple_xor_decrypt(encrypted_test, test_key)
        
        # Check if perfect
        is_perfect = np.array_equal(test_image, decrypted_test)
        
        # Display results
        st.markdown("**Test Results:**")
        
        col_test1, col_test2, col_test3 = st.columns(3)
        
        with col_test1:
            st.image(test_image, caption="Original", use_column_width=True)
            st.caption("Original Test Image")
        
        with col_test2:
            st.image(encrypted_test, caption="Encrypted", use_column_width=True)
            st.caption("Encrypted (should look random)")
        
        with col_test3:
            st.image(decrypted_test, caption="Decrypted", use_column_width=True)
            st.caption("Decrypted (should match original)")
        
        if is_perfect:
            st.markdown('<div class="success-box">', unsafe_allow_html=True)
            st.success("✅ **TEST PASSED:** Perfect encryption and decryption!")
            st.write("All pixels match exactly. The algorithm is working correctly.")
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Calculate differences
            diff = np.sum(np.abs(test_image.astype(int) - decrypted_test.astype(int)))
            diff_percent = (diff / test_image.size) * 100
            
            st.error(f"❌ **TEST FAILED:** Total pixel difference = {diff}")
            st.error(f"Difference percentage: {diff_percent:.6f}%")
            
            # Show difference image
            diff_image = np.abs(test_image.astype(int) - decrypted_test.astype(int))
            diff_image = np.clip(diff_image * 50, 0, 255).astype(np.uint8)
            
            st.image(diff_image, caption="Difference (amplified 50x)", width=300)

st.markdown('</div>', unsafe_allow_html=True)

# Information section
with st.expander("📚 How It Works", expanded=False):
    st.markdown("""
    ### XOR Image Encryption Algorithm
    
    **Encryption Process:**
    1. **Key Processing:**
       - User enters a text key (e.g., "MySecretKey123")
       - SHA-256 cryptographic hash is computed from the key
       - Hash produces 256 bits (32 bytes) of deterministic data
       
    2. **Key Expansion:**
       - Hash bytes are repeated to match the image size
       - For example, a 100×100 RGB image needs 30,000 bytes (100×100×3)
       - Hash bytes are repeated until we have enough bytes
       
    3. **XOR Operation:**
       - Each pixel value (0-255) is XORed with corresponding key byte
       - XOR is a bitwise operation: 1 if bits differ, 0 if same
       - Formula: `Encrypted = Image ⊕ Key`
       
    4. **Result:**
       - Produces encrypted image that looks like random noise
       - Same dimensions as original
       - Saved as PNG format
    
    **Decryption Process:**
    - Same key generates identical byte sequence
    - XOR is symmetric: `(A ⊕ B) ⊕ B = A`
    - Formula: `Decrypted = Encrypted ⊕ Key`
    - Perfect reconstruction with correct key
    
    **Mathematical Properties:**
    - **Perfect Reversibility:** XOR operation is mathematically reversible
    - **Deterministic:** Same key always produces same encryption/decryption
    - **Fast:** Simple bitwise operations
    - **Lossless:** No data compression or quality loss
    
    **Security Characteristics:**
    - **Key Sensitivity:** Tiny key changes produce completely different results
    - **Avalanche Effect:** Small input changes cause large output changes
    - **Uniform Distribution:** Encrypted pixels appear random
    
    **Example:**
    ```
    Original Pixel: 150 = 10010110 (binary)
    Key Byte:        73 = 01001001 (binary)
    XOR Result:     223 = 11011111 (binary)  ← Encrypted
    
    To Decrypt:
    Encrypted:      223 = 11011111
    Key Byte:        73 = 01001001
    XOR Result:     150 = 10010110  ← Perfect recovery!
    ```
    
    **Note for Educational Use:**
    This is a **simplified** implementation demonstrating XOR encryption.
    For real-world security applications, use established cryptographic
    libraries with proper encryption standards (AES, RSA, etc.).
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