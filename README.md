# Frida AES Hook - Bypassing encryption in android apps

A **frida script** for intercepting and analyzing **AES encryption** in Android applications in real time.  
Ideal for **penetration testing, reverse engineering, and security researcher.**  

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
frida -U -f <package name> -l /path/enc.js --no-auto-reload
```

## How the script works ?
This script hooks into java’s cryptographic functions and intercepts key operations like:
- `Cipher.init(mode, key, params)` => captures the encryption/decryption mode, AES key, and IV before they are used.
- `Cipher.doFinal(data)` => logs plaintext before encryption and ciphertext after decryption.
- `SecretKeySpec` constructor => extracts AES key during initialization.
- `IvParameterSpec` constructor => retrieves IV when it is generated.
  
By hooking into these methods, it is possible to monitor how encryption is performed without modifying the app’s source code.

## Example output
Once running, the script will log encryption-related data like this:
```sh
Mode: encrypt
Key : b'Secret_Key'
IV  : b'Iv'
data: b'plaintext'
```
During decryption:
```sh
Mode: decrypt
Key : b'Secret_Key'
IV  : b'Iv'
data: b'ciphertext'
```
This output provides valuable insights into how the application handles encryption, helping in security analysis or debugging.

## Reference
- **Frida**  
  https://codeshare.frida.re/@dzonerzy/aesinfo/

- **Cognisys Labs**  
  https://labs.cognisys.group/posts/Breaking-Custom-Ecryption-Using-Frida-Mobile-Application-pentesting/

- **infosecwriteups**  
  https://infosecwriteups.com/analyzing-android-encryption-processes-with-frida-a3ab2622fce9

- **Android Developer**  
  https://developer.android.com/reference/javax/crypto/spec/SecretKeySpec  
  https://developer.android.com/reference/javax/crypto/spec/IvParameterSpec  
  https://developer.android.com/reference/java/security/spec/AlgorithmParameterSpec

- **Wikipedia**  
  https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
