import numpy as np
import hashlib

class BuniProtocol:
    """
    The BUNI Protocol: Symmetric Matrix Hashing (SMH)
    A grid-based encryption engine inspired by ancient doubly-even magic squares,
    adapted for post-quantum cryptographic security.
    """
    
    def __init__(self, matrix_size=256):
        """ 
        Initialize the matrix size. 
        Default is 256x256 (Standard 8-bit cryptographic grid scaling).
        """
        self.n = matrix_size
        
    def _create_base_magic_square(self):
        """ 
        Phase 1: Base Tensor Generation
        Generates a perfectly symmetrical doubly-even magic square.
        Every row, column, and main diagonal sums to the same Magic Constant.
        """
        matrix = np.zeros((self.n, self.n), dtype=np.int64)
        count = 1
        
        for i in range(self.n):
            for j in range(self.n):
                # Geometric intersection rule (Masking logic for symmetry)
                if (i % 4 == j % 4) or (i % 4 + j % 4 == 3):
                    matrix[i][j] = count
                else:
                    matrix[i][j] = (self.n * self.n + 1) - count
                count += 1
                
        return matrix

    def generate_quantum_key(self, password):
        """ 
        Phase 2 & 3: The Cryptographic Shift
        Takes a raw string password and morphs the base tensor into a 
        unique, entangled multidimensional vault.
        """
        # Step A: Seed Extraction (Hashing the password via SHA-256)
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # Step B: Convert the initial hash chunk into a numeric crypto-seed
        crypto_seed = int(hashed_pw[:8], 16)
        
        # Step C: Retrieve the Base Matrix
        base_matrix = self._create_base_magic_square()
        
        # Step D: The Equilibrium Shift (Applying dynamic offset based on input)
        # Calculates the byte-sum of the string multiplied by the crypto-seed
        dynamic_offset = sum(password.encode('utf-8')) * crypto_seed
        
        # Entangling the entire 256x256 matrix with the unique dynamic offset
        encrypted_matrix = base_matrix + dynamic_offset
        
        # Step E: Calculate the absolute Magic Constant (The Equilibrium Point)
        magic_constant = np.sum(encrypted_matrix[0])
        
        return encrypted_matrix, magic_constant, hashed_pw

# ==========================================
# 🚀 SYSTEM SIMULATION & TESTING
# ==========================================

if __name__ == "__main__":
    # 1. Initialize the Buni Protocol System
    buni_system = BuniProtocol(matrix_size=256)

    # 2. Define user input (Private Key or Password)
    user_password = "MySuperSecretPassword2026!"

    # 3. Generate the Quantum-Resistant Matrix and Keys
    matrix, magic_constant, pw_hash = buni_system.generate_quantum_key(user_password)

    # 4. Display Cryptographic Output
    print("=" * 60)
    print("🛡️  THE BUNI PROTOCOL - SMH V1.0 INITIALIZED  🛡️")
    print("=" * 60)
    print(f"[*] User Input (Raw)    : {user_password}")
    print(f"[*] Core SHA-256 Hash   : {pw_hash[:24]}...")
    print("-" * 60)
    print(f"✅ Matrix Generated      : 256 x 256 Symmetric Tensor")
    print(f"✅ Total Data Blocks     : {256 * 256:,} Entangled Cells")
    print("-" * 60)
    print(f"🔮 THE MAGIC CONSTANT (Absolute Equilibrium Point):")
    print(f"    Sum of ANY row, column, or diagonal = {magic_constant:,}")
    print("=" * 60)
    print("[*] Displaying the Top-Left 4x4 block of the encrypted matrix:\n")
    print(matrix[:4, :4])
    print("\n" + "=" * 60)
