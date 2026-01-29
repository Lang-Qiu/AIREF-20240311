import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from . import settings

PRIVATE_KEY_PATH = settings.PRIVATE_KEY_PATH


def get_key(key_file):
    with open(key_file) as f:
        data = f.read()
        key = RSA.importKey(data)

    return key


def decrypt(encrypt_msg):
    private_key = get_key(PRIVATE_KEY_PATH)
    cipher = PKCS1_cipher.new(private_key)
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)
    return back_text.decode("utf-8")
