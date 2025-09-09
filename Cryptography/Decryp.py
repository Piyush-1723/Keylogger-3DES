import os
from Crypto.Cipher import DES3

# Project root = Almost_Kelogger
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure Logs folder exists
LOGS_DIR = os.path.join(PROJECT_DIR, "Logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Ensure Cryptography folder exists
CRYPTO_DIR = os.path.join(PROJECT_DIR, "Cryptography")
os.makedirs(CRYPTO_DIR, exist_ok=True)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f_in:
        iv = f_in.read(8)
        ciphertext = f_in.read()

    cipher = DES3.new(key, DES3.MODE_OFB, iv)
    plaintext = cipher.decrypt(ciphertext)

    with open(output_file, 'wb') as f_out:
        f_out.write(plaintext.rstrip(b'\0'))

# Load key
key_path = os.path.join(CRYPTO_DIR, "enc_dec.k3des")
with open(key_path, "rb") as f:
    key = f.read()

# Decrypt latest.elog → decrypted.dlog
encrypted_file = os.path.join(LOGS_DIR, "latest.elog")
decrypted_file = os.path.join(LOGS_DIR, "decrypted.dlog")

decrypt_file(encrypted_file, decrypted_file, key)
print(f"[+] Decryption complete → {decrypted_file}")
