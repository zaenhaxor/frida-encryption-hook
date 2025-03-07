# Frida AES Hook - Bypassing encryption in android apps

A **Frida script** for intercepting and analyzing **AES encryption** in Android applications in real time.  
Ideal for **penetration testing, reverse engineering, and security research.**  

---

## Features
- **Extracts AES Secret Key** before it is used.  
- **Retrieves IV (Initialization Vector)** for encryption.  
- **Captures plaintext before encryption & ciphertext after decryption.**  
- Hooks into Java **`Cipher`**, **`SecretKeySpec`**, and **`IvParameterSpec`**.  
- Ensures the application continues running smoothly.  

---

## Run the script and analyze
After installing Frida, run the script against the target application: 
```sh
**frida -U -f <package name> -l /path/enc.js --no-auto-reload
---
