import hashlib

def calculate_checksum(file_path, algo='md5'):
    hash_func = getattr(hashlib, algo)()

    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)

    return hash_func.hexdigest()
