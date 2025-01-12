**Description:**
This Python project demonstrates how to use AES encryption to securely encrypt and decrypt image files. The script leverages the pycryptodome library for cryptographic operations and provides an easy-to-use CLI (Command Line Interface) for users to encrypt or decrypt image files with a custom key.

**Features:**
Encrypt any image file using AES encryption with ECB mode.
Decrypt encrypted image files to restore the original image.
Padding and unpadding of data are handled automatically.
CLI support with options for file paths, key input, and encryption/decryption mode.

**How to Use:**
Provide the input file path, output file path, and a key using the command line.
Use the --decrypt flag to switch from encryption to decryption.

**(Example Commands:)**

**Encrypt an image:**
python script.py input.jpg encrypted_output.jpg --key your_key

**Decrypt an image:**
python script.py encrypted_output.jpg decrypted_output.jpg --key your_key --decrypt

**Dependencies:**
pycryptodome

**Note:** The script uses AES in ECB mode, which does not involve an initialization vector (IV). For production use, consider a more secure mode like CBC or GCM.
