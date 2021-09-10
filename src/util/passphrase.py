import random
import os

BLOCK_SIZE = 128

def generate_key():
    key = []
    n = random.randint(0, 0xffffffffffffffffffffffffffffffff)
    for i in range(int(BLOCK_SIZE/8)):
        key.append(n&0xff)
        n >>= 8

    id_key = len(os.listdir('../keys'))
    filename = f'key_{id_key}'
    with open(f'../keys/{filename}', "wb") as f:
        f.write(bytes(key))

    print("A chave gerada foi salva no arquivo", filename, "da pasta keys")
    return key

def parse_key(key_file):
    key = []
    with key_file as f:
        byte = f.read(1)
        while byte != b"":
            key.append(ord(byte))
            byte = f.read(1)

    if is_valid(key):
        return key
    else:
        raise Exception(f"Chave inválida! As chaves devem ter exatamente {BLOCK_SIZE} bits de tamanho")

def is_valid(key):
    return len(key) == BLOCK_SIZE/8
    