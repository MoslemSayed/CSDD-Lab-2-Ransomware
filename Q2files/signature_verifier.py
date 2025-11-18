import os
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

public_key = RSA.import_key(open("publickey.pem", "rb").read())

for file in os.listdir("."):
    if file.endswith(".exe"):
        with open(file, "rb") as f:
            data = f.read()
        h = SHA256.new(data)
        signature = open(file + ".sign", "rb").read()
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            print("Signature is valid for file:", file)
        except (ValueError, TypeError):
            print("Signature is NOT valid for file:", file)