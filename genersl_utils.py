def read_key(file_pub):
    """Read public key from file"""
    with open(file_pub, 'r') as file:
        key = file.read()
    return key
