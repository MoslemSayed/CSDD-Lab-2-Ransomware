'''
Victim Decryption Program
'''

import os
import sys
from cryptography.fernet import Fernet

def main():
    print("Enter decryption key:")
    shared_key = sys.stdin.readline().strip().encode()

    fernet = Fernet(shared_key)

    for filename in os.listdir("."):
        if filename.endswith(".txt.encrypted"):
            with open(filename, "rb") as f:
                encrypted_data = f.read()

            decrypted_data = fernet.decrypt(encrypted_data)

            # restore original name
            original_name = filename.replace(".encrypted", "")

            with open(original_name, "wb") as f:
                f.write(decrypted_data)

            os.remove(filename)

    print("Decryption completed.")

if __name__ == "__main__":
    main()
