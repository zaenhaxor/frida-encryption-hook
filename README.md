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
```

# How the Script Works

This script hooks into Java’s cryptographic functions and intercepts key operations like:

- `Cipher.init(mode, key, params)` → Captures the encryption/decryption mode, AES key, and IV before they are used.
- `Cipher.doFinal(data)` → Logs plaintext before encryption and ciphertext after decryption.
- `SecretKeySpec` constructor → Extracts AES key during initialization.
- `IvParameterSpec` constructor → Retrieves IV when it is generated.

By hooking into these methods, we can monitor how encryption is performed without modifying the app’s source code.

## Example Output

Once running, the script will log encryption-related data like this:

```sh
Mode: encrypt
Key : b'SECRET_AES_KEY_HERE'
IV  : b'INITIALIZATION_VECTOR_HERE'
data: b'PLAINTEXT_BEFORE_ENCRYPTION'
```

During decryption:

```sh
Mode: decrypt
Key : b'SECRET_AES_KEY_HERE'
IV  : b'INITIALIZATION_VECTOR_HERE'
data: b'CIPHERTEXT_BEFORE_DECRYPTION'
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
