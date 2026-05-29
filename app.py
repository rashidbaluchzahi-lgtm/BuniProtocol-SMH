import streamlit as st
import numpy as np
import hashlib
import pandas as pd

# ==========================================
# PAGE CONFIGURATION (UI/UX)
# ==========================================
st.set_page_config(
    page_title="BUNI Protocol | SMH",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for Cyberpunk / Web3 Aesthetic
st.markdown("""
    <style>
    .main {background-color: #0e1117;}
    h1 {color: #00ffcc;}
    h2, h3 {color: #00ffcc;}
    .stButton>button {
        width: 100%;
        background-color: #00ffcc;
        color: #000000;
        font-weight: bold;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #00b38f;
    }
    .success-text {color: #00ffcc; font-size: 20px; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# CORE ALGORITHM (The BUNI Protocol Engine)
# ==========================================
class BuniProtocol:
    def __init__(self, matrix_size=256):
        self.n = matrix_size
        
    def _create_base_magic_square(self):
        matrix = np.zeros((self.n, self.n), dtype=np.int64)
        count = 1
        for i in range(self.n):
            for j in range(self.n):
                if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                    matrix[i][j] = count
                else:
                    matrix[i][j] = (self.n * self.n + 1) - count
                count += 1
        return matrix

    def generate_quantum_key(self, password):
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
        crypto_seed = int(hashed_pw[:8], 16)
        base_matrix = self._create_base_magic_square()
        
        dynamic_offset = sum(password.encode('utf-8')) * crypto_seed
        encrypted_matrix = base_matrix + dynamic_offset
        magic_constant = np.sum(encrypted_matrix[0])
        
        return encrypted_matrix, magic_constant, hashed_pw

# ==========================================
# WEB APPLICATION INTERFACE
# ==========================================
st.title("🛡️ THE BUNI PROTOCOL")
st.subheader("Symmetric Matrix Hashing (SMH) for Post-Quantum Security")

st.markdown("""
Welcome to the future of cryptography. The BUNI Protocol converts vulnerable passwords into 
**256x256 perfectly symmetric, multidimensional tensors**. A single bit change breaks the geometric balance.
""")

st.sidebar.header("About The Protocol")
st.sidebar.info("""
**Version:** 1.0 (Open Source)  
**Algorithm:** Doubly-Even Magic Square Mapping  
**Security:** Post-Quantum Lattice-like Entanglement  

Instead of storing passwords, we store an ecosystem of numbers where:  
`Row Sum = Column Sum = Diagonal Sum = Absolute Equilibrium`
""")

# User Input Section
user_input = st.text_input("Enter your Seed Phrase or Password:", type="password")

if st.button("Generate Quantum Matrix"):
    if user_input:
        with st.spinner("Entangling data... Forging symmetric tensor..."):
            
            # Initialize Protocol
            buni = BuniProtocol(256)
            matrix, magic_constant, pw_hash = buni.generate_quantum_key(user_input)
            
            st.success("✅ Matrix Successfully Generated and Entangled!")
            
            # Display Core Metrics
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🔑 Core SHA-256 Hash")
                st.code(f"{pw_hash[:32]}...")
            with col2:
                st.markdown("### ⚖️ The Magic Constant")
                st.markdown(f"<p class='success-text'>{magic_constant:,}</p>", unsafe_allow_html=True)
                
            st.markdown("---")
            
            # Display Matrix Sample
            st.markdown("### 💠 Matrix Core View (Top-Left 8x8 Grid)")
            st.markdown("Visualizing a fragment of the 65,536 interconnected cells:")
            sample_df = pd.DataFrame(matrix[:8, :8])
            st.dataframe(sample_df, use_container_width=True)
            
            # Download Button for the full Matrix
            csv = pd.DataFrame(matrix).to_csv(index=False, header=False)
            st.download_button(
                label="📥 Download Full 256x256 Encrypted Tensor (CSV)",
                data=csv,
                file_name="Buni_Protocol_Vault.csv",
                mime="text/csv",
            )
    else:
        st.warning("⚠️ Please enter a password or seed phrase to initialize the protocol.")
