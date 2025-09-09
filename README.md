# 🔑 Keylogger with Triple DES (3DES) Encryption  

## 📌 Project Overview  
This project implements a **keylogger** that records keystrokes and protects the logs using **Triple DES (3DES) encryption**.  
It is built as an **educational project** to demonstrate how cryptography can safeguard sensitive log data.  

---

## 🚀 Features  
- ⌨️ **Keystroke Logging** – captures all key presses.  
- 🕒 **Timestamped Logs** – each run creates uniquely named log files.  
- 🖥️ **Metadata Header** – logs include system info, session timestamp, and duration.  
- 🔒 **Triple DES Encryption** – raw logs are encrypted securely after capture.  
- 🔑 **Custom Key Format** – encryption key stored as `.k3des`.  
- 📂 **Custom Extensions** –  
  - Raw logs → `.log`  
  - Encrypted logs → `.elog`  
  - Decrypted logs → `.dlog`  
  - Key file → `.k3des`  
- ⌛ **CLI Duration Control** – specify logging duration with `--duration`.  

---

## 📂 Project Structure  

```
Almost_Kelogger/
│
├── Cryptography/
│   ├── Encryp.py       # Generate encryption key (.k3des)
│   ├── Decryp.py       # Decrypt latest encrypted log
│   └── enc_dec.k3des   # Encryption key (auto-generated, ignored in Git)
│
├── Keylogger/
│   └── Keylog.py       # Main keylogger (timestamped logs, metadata, CLI)
│
├── Logs/
│   ├── key_log_2025-09-09_12-00-00.log   # Raw keystrokes (example)
│   ├── e_key_log_2025-09-09_12-00-00.elog # Encrypted logs (example)
│   ├── latest.elog                        # Copy of most recent encrypted log
│   └── decrypted.dlog                     # Decrypted log from latest.elog
│
├── requirements.txt   # Dependencies (pycryptodome, pynput)
├── .gitignore         # Ignore logs/keys in Git
└── README.md          # Documentation
```

---

## ⚙️ Installation  

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage  

### 1. Generate Encryption Key  
```bash
python Cryptography/Encryp.py
```
👉 Creates `enc_dec.k3des` inside `Cryptography/`.  

---

### 2. Run Keylogger  
Default (10 seconds logging):  
```bash
python Keylogger/Keylog.py
```

Custom duration (e.g., 20 seconds):  
```bash
python Keylogger/Keylog.py --duration 20
```

👉 Creates logs like:  
- `key_log_2025-09-09_12-00-00.log` (raw keystrokes)  
- `e_key_log_2025-09-09_12-00-00.elog` (encrypted log)  
- `latest.elog` (easy decryption reference)  

---

### 3. Decrypt Logs  
```bash
python Cryptography/Decryp.py
```
👉 Decrypts `latest.elog` into `decrypted.dlog`.  

---

## ⚠️ Disclaimer  
> This project is for **educational and research purposes only**.  
> Do **NOT** use it on systems without explicit permission.  
> Unauthorized use of keyloggers is **illegal**.  

---
