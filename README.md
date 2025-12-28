# Multi-Algorithm Encryption Suite

A comprehensive web application implementing multiple encryption algorithms for both text and images, built with Streamlit for educational and demonstration purposes.

![Encryption Suite](https://img.shields.io/badge/Encryption-Suite-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Table of Contents

- [Features](#-features)
- [Live Demo](#-live-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Algorithms](#-algorithms)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## Features

### Text Encryption Algorithms

**Classical Ciphers:**
- Transposition Cipher
- Caesar Cipher
- Affine Cipher
- Hill Cipher (with matrix operations)
- Vigenere Cipher

**Modern Ciphers (Simplified Educational Versions):**
- DES (Data Encryption Standard)
- AES (Advanced Encryption Standard)
- RSA (Public-Key Cryptography)

### Image Encryption

- Chaotic Image Encryption using logistic map
- Supports both RGB and grayscale images
- Lossless encryption/decryption
- Download encrypted/decrypted images

### Key Features

- **Interactive Web Interface**: Built with Streamlit for easy access
- **Real-time Encryption/Decryption**: Instant results with visual feedback
- **Educational Focus**: Detailed explanations for each algorithm
- **Clean Design**: Professional and intuitive user interface
- **Cross-platform**: Works on any device with a web browser
- **No Installation Required**: Run locally or deploy to cloud

## Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

> **Note:** Replace with your actual deployment URL

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step-by-Step Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/encryption-suite.git
cd encryption-suite
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
streamlit run app.py
```

5. **Open your browser** and navigate to `http://localhost:8501`

##  Usage

### Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

### Using Text Encryption:

1. Select an algorithm from the sidebar dropdown
2. Enter plain text in the encryption section
3. Provide necessary parameters (key, shift value, matrix, etc.)
4. Click "Encrypt" to see the result
5. Use the same parameters in the decryption section to decrypt

### Using Image Encryption:

1. Select "Image Encryption" from the sidebar
2. Upload an image (JPG, PNG, BMP)
3. Enter an encryption key
4. Click "Encrypt Image"
5. Download the encrypted image
6. Use the same key to decrypt

##  Algorithms

### Text Encryption Algorithms

#### 1. Transposition Cipher
- **Type:** Transposition
- **Key:** String that determines column order
- **Description:** Rearranges characters according to a specific pattern

#### 2. Caesar Cipher
- **Type:** Substitution
- **Key:** Integer shift value (0-25)
- **Description:** Each letter is shifted a fixed number of positions

#### 3. Affine Cipher
- **Type:** Mathematical substitution
- **Key:** Two integers (a, b) where a must be coprime with 26
- **Formula:** `E(x) = (ax + b) mod 26`

#### 4. Hill Cipher
- **Type:** Polygraphic substitution
- **Key:** 2×2 matrix with determinant coprime to 26
- **Description:** Encrypts blocks of text using matrix multiplication

#### 5. Vigenere Cipher
- **Type:** Polyalphabetic substitution
- **Key:** Keyword repeated to match text length
- **Description:** Uses multiple Caesar ciphers based on keyword

#### 6. DES (Simplified)
- **Type:** Symmetric block cipher (educational version)
- **Key:** 8-character string
- **Note:** Simplified implementation for educational purposes

#### 7. AES (Simplified)
- **Type:** Symmetric block cipher (educational version)
- **Key:** Any string (converted to SHA-256 hash)
- **Note:** Simplified implementation for educational purposes

#### 8. RSA (Simplified)
- **Type:** Public-key cryptosystem (educational version)
- **Key:** Automatically generated key pair
- **Note:** Uses small primes for demonstration

### Image Encryption

#### Chaotic Image Encryption
- **Type:** XOR-based symmetric encryption with chaotic maps
- **Key:** Any string (converted to SHA-256 hash)
- **Process:**
  1. Key → SHA-256 hash
  2. Generate chaotic sequence using logistic map
  3. XOR operation between pixels and key stream
  4. Lossless recovery with same key
- **Features:** Supports RGB and grayscale, preserves dimensions

##  Project Structure

```
multi-encryption-suite/
│
├── app.py                    # Main Streamlit app
├── utils.py                  # Common utility functions
├── requirements.txt          # Dependencies
│
├── text_encryption/
│   ├── __init__.py
│   ├── transposition.py
│   ├── caesar.py
│   ├── affine.py
│   ├── hill.py
│   ├── vigenere.py
│   ├── des.py
│   ├── aes.py
│   └── rsa.py
│
├── image_encryption/
│   ├── __init__.py
│   └── chaotic_encryption.py
│
└── pages/
    ├── Home.py
    ├── text_Encryption.py
    └── image_Encryption.py
```

### Key Files

- **app.py**: Contains all encryption/decryption algorithms and Streamlit UI
- **requirements.txt**: Lists all Python dependencies
- **README.md**: Project documentation

##  Screenshots
### App interface
![Home Page](screenshots/app.png)

### Home Interface
![Home Page](screenshots/home.png)

### Text Encryption (Hill Cipher)
![Hill Cipher](screenshots/text_encryption_example.png)

### Image Encryption
![Image Encryption](screenshots/image-encryption.mp4)

> **Note:** Add actual screenshots to a `screenshots/` directory

##  Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**

2. **Create a feature branch**
```bash
git checkout -b feature/AmazingFeature
```

3. **Commit your changes**
```bash
git commit -m 'Add some AmazingFeature'
```

4. **Push to the branch**
```bash
git push origin feature/AmazingFeature
```

5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 coding standards
- Add comments for complex algorithms
- Update documentation as needed
- Test your changes thoroughly

## Important Security Notice

> **This application is for EDUCATIONAL PURPOSES ONLY.**

### Security Limitations:
- Simplified implementations are NOT cryptographically secure
- Do NOT use for real-world sensitive data
- Algorithms use reduced key sizes and simplified operations
- For production use, always use verified cryptographic libraries

### Recommended for Real Applications:
- **Text:** Use `cryptography` library (proper AES, RSA implementations)
- **Images:** Use OpenCV with proper encryption standards
- **General:** Use established libraries like `PyCryptodome`, `NaCl`


Copyright (c) 2025 [Amine EL HANINE]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Author

**Your Name**

- GitHub: [@yourusername](https://github.com/l7a9)
- Email: melhanineamine@gmail.com
- LinkedIn: [Your Profile](https://www.linkedin.com/in/amine-el-hanine-88689a330/)

## Acknowledgments

- Streamlit team for the amazing framework
- Cryptography community for algorithm references
- Open source contributors who make education accessible
- Professors and educators in the field of cryptography


**If you find this project useful, please give it a star on GitHub!**

---

### Requirements.txt

Create a `requirements.txt` file with the following dependencies:

```
altair==6.0.0
attrs==25.4.0
blinker==1.9.0
cachetools==6.2.4
certifi==2025.11.12
charset-normalizer==3.4.4
click==8.3.1
contourpy==1.3.3
cycler==0.12.1
Flask==3.1.2
fonttools==4.61.1
gitdb==4.0.12
GitPython==3.1.45
idna==3.11
itsdangerous==2.2.0
Jinja2==3.1.6
jsonschema==4.25.1
jsonschema-specifications==2025.9.1
kiwisolver==1.4.9
MarkupSafe==3.0.3
matplotlib==3.10.8
mpmath==1.3.0
narwhals==2.14.0
numpy==2.2.6
opencv-python==4.12.0.88
packaging==25.0
pandas==2.3.3
pillow==12.0.0
protobuf==6.33.2
pyarrow==22.0.0
pycryptodome==3.23.0
pydeck==0.9.1
pyparsing==3.3.1
python-dateutil==2.9.0.post0
pytz==2025.2
referencing==0.37.0
requests==2.32.5
rpds-py==0.30.0
six==1.17.0
smmap==5.0.2
streamlit==1.52.2
sympy==1.14.0
tenacity==9.1.2
toml==0.10.2
tornado==6.5.4
typing_extensions==4.15.0
tzdata==2025.3
urllib3==2.6.2
watchdog==6.0.0
Werkzeug==3.1.4

```

###  Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/yourusername/encryption-suite.git
cd encryption-suite
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

**Made with ❤️ and Python**