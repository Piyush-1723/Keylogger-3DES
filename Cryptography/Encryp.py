import os
from Crypto.Random import get_random_bytes

# Project root = Almost_Kelogger
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure Cryptography folder exists
CRYPTO_DIR = os.path.join(PROJECT_DIR, "Cryptography")
os.makedirs(CRYPTO_DIR, exist_ok=True)

def generate_valid_tdes_key():
    return get_random_bytes(24)  # 24 bytes = 3DES key

tdes_key = generate_valid_tdes_key()
print("Generated Triple DES key:", tdes_key.hex())

# Save key with custom extension
key_path = os.path.join(CRYPTO_DIR, "enc_dec.k3des")
with open(key_path, "wb") as file:
    file.write(tdes_key)

print(f"[+] Key saved to {key_path}")
