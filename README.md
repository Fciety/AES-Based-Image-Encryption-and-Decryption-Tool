**Description:**

This Python script uses AES encryption to encrypt and decrypt image files. It leverages the pycryptodome library for cryptographic operations and provides a simple CLI for encrypting or decrypting files with a custom key. It handles padding/unpadding automatically and supports file paths, key input, and encryption/decryption modes.

**Features:**

Encrypt and decrypt image files using AES (ECB mode).
Automatically handles padding and unpadding of data.
CLI for specifying input/output paths and key.

**How to Use:**

Provide file paths and a key via the command line.
Use --decrypt flag to decrypt an image.

**Example Commands:**

**Encrypt:** python script.py input.jpg encrypted.jpg --key key

**Decrypt:** python script.py encrypted.jpg output.jpg --key key --decrypt

**Dependencies:**

pycryptodome

**Note:**
The script uses AES in ECB mode, which does not use an IV. For better security, consider using CBC or GCM.
