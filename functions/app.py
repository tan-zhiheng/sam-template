from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


# a function to generate key pairs
def generate_key_pair(key_size=2048):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)

    public_key = private_key.public_key()

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode("utf-8")

    public_key_pub = public_key.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH,
    ).decode("utf-8")
    print(f"private key: {private_key_pem}")
    print(f"public key: {public_key_pub}")
    print("keys generated")

    return private_key_pem, public_key_pub


# aws lambda function handler
def handler(event, context):
    print(f"event: {event}")
    print(f"context: {context}")
    private_key_pem, public_key_pub = generate_key_pair()
    return {"private_key_pem": private_key_pem, "public_key_pub": public_key_pub}
