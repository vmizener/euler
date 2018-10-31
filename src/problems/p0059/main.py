from itertools import cycle, product
from functools import reduce
from operator import add, xor
from time import time

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def main():
    with open('cipher.txt', 'r') as fh:
        cipher = [int(el) for el in fh.readline().strip().split(',')]
    ret = {}
    res = ''
    for key in product(LETTERS, repeat=3):
        keyiter = cycle(map(ord, key))
        candidate = reduce(add, map(lambda pair: chr(xor(*pair)), zip(keyiter, cipher)))
        if 'the ' in candidate and 'in ' in candidate and 'and ' in candidate:
            res = candidate
            ret['key'] = reduce(add, key)
            break
    ret['text'] = res
    ret['sum'] = sum(map(ord, res))
    return ret
