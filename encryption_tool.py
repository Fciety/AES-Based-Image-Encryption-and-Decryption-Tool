from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import argparse

# Function to encrypt an image file
def encrypt_image(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as f:
            image_data = f.read()

        cipher = AES.new(key, AES.MODE_ECB)

        padded_data = pad(image_data, AES.block_size)

        encrypted_data = cipher.encrypt(padded_data)

        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

        print("Encryption completed.")
    except FileNotFoundError:
        print("Error: Input file not found.")

# Function to decrypt an image file
def decrypt_image(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()

        cipher = AES.new(key, AES.MODE_ECB)

        decrypted_data = cipher.decrypt(encrypted_data)

        unpadded_data = unpad(decrypted_data, AES.block_size)

        with open(output_file, 'wb') as f:
            f.write(unpadded_data)

        print("Decryption completed.")
    except FileNotFoundError:
        print("Error: Input file not found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encrypt or decrypt an image file using AES encryption.')
    parser.add_argument('input_file', type=str, help='Path to the input image file')
    parser.add_argument('output_file', type=str, help='Path to the output image file')
    parser.add_argument('--key', type=str, default=None, help='Encryption key (required)')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the input file')

    args = parser.parse_args()

    if args.key is None:
        parser.error("Encryption key is required.")
    else:
        key = bytes(args.key, 'utf-8')

        if args.decrypt:
            decrypt_image(args.input_file, args.output_file, key)
        else:
            encrypt_image(args.input_file, args.output_file, key)
