from math import sqrt
from functools import reduce

def is_triangular(n):
    return ((sqrt(1+8*n)-1)/2).is_integer()

def word_value(word):
    return reduce(lambda x, y: x+ord(y)-64, word, 0)

def main():
    with open('words.txt', 'r') as fh:
        words = fh.readline().strip().replace('"', '').split(',')
    triangle_words = set()
    for word in words:
        if is_triangular(word_value(word)):
            triangle_words.add(word)
    return len(triangle_words)
