# Code inspired by
# http://programeveryday.com/post/implementing-a-basic-vigenere-cipher-in-python/

# version with encrypter
# https://gist.github.com/jcemelanda/cba27615f50b2c80cbcd5fc1188d4f43

from itertools import cycle
from functools import reduce

ALPHA_LOW = 'abcdefghijklmnopqrstuvwxyz'
ALPHA_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        if pair[0] in ALPHA_LOW:
            total = reduce(
                lambda x, y: ALPHA_LOW.index(x) - ALPHA_LOW.index(y),
                pair
            )
            result += ALPHA_LOW[total % 26]
        elif pair[0] in ALPHA_UPPER:
            total = reduce(
                lambda x, y: ALPHA_UPPER.index(x) - ALPHA_LOW.index(y),
                pair
            )
            result += ALPHA_UPPER[total % 26]
        else:
            result += pair[0]

    return result
