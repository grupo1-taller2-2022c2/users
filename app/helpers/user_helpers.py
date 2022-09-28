import hashlib


def hash_password(password):
    return int(hashlib.sha256(password.encode('utf-8')).hexdigest(), 16) % 10**8
