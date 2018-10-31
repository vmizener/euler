from time import time

def score(name, pos):
    ret = 0
    for c in name:
        ret += ord(c)-64
    return pos*ret

def main():
    with open('names.txt', 'r') as fh:
        names = fh.readline().strip().replace('"', '').split(',')
    sum = 0
    for pos, name in enumerate(sorted(names)):
        sum += score(name, pos+1)
    return sum
