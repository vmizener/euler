from math import sqrt
from time import time
from tools import gen_primes

def gen_composite_odds():
    cur = 3
    gp = gen_primes()
    next_prime = gp.next()
    while True:
        while cur > next_prime:
            next_prime = gp.next()
        if cur < next_prime:
            yield cur
        cur += 2

def f():
    for c in gen_composite_odds():
        goldbach = False
        for p in gen_primes():
            if c <= p:
                break
            if sqrt((c-p)/2.0).is_integer():
                goldbach = True
                break
        if not goldbach:
            return c

if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s, 'seconds'