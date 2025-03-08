from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import argparse

#untuk mengenkripsi data dgn AES-256-CBC
def encrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return b64encode(ciphertext).decode()

#untuk mendekripsi data yg telah dienkripsi dgn AES-256-CBC
def decrypt(data, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = b64decode(data)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()

def main():
    parser = argparse.ArgumentParser(
        description="Tools enkrip & dekrip AES-256 \n"
                    "Tools ini untuk mengenkripsi atau mendekripsi teks dengan metode AES-256-CBC.\n"
                    "Secret key yg digunakan harus memiliki panjang 32 byte dan IV 16 byte.\n",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help="Pilih salah satu:")

    encrypt_parser = subparsers.add_parser('encrypt', help='Enkripsi teks')
    encrypt_parser.add_argument('-data', required=True, help='Teks yg ingin dienkripsi')
    encrypt_parser.add_argument('-key', required=True, help='Secret Key (32 byte)')
    encrypt_parser.add_argument('-iv', required=True, help='IV (16 byte)')

    decrypt_parser = subparsers.add_parser('decrypt', help='Dekripsi teks')
    decrypt_parser.add_argument('-data', required=True, help='Teks terenkripsi yg ingin didekripsi')
    decrypt_parser.add_argument('-key', required=True, help='Secret key yg digunakan saat enkripsi')
    decrypt_parser.add_argument('-iv', required=True, help='IV yg digunakan saat enkripsi')

    args = parser.parse_args()

    if args.command == 'encrypt':
        try:
            encrypted_data = encrypt(args.data, args.key.encode(), args.iv.encode())
            print(f"hasil enkrip:{encrypted_data}")
        except Exception as e:
            print(f"error: {e}")

    elif args.command == 'decrypt':
        try:
            decrypted_data = decrypt(args.data, args.key.encode(), args.iv.encode())
            print(f"hasil dekrip: {decrypted_data}")
        except Exception as e:
            print(f"error: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
