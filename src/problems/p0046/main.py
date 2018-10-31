from math import sqrt
from ...utils.primes import gen_primes

def gen_composite_odds():
    cur = 3
    gp = gen_primes()
    next_prime = next(gp)
    while True:
        while cur > next_prime:
            next_prime = next(gp)
        if cur < next_prime:
            yield cur
        cur += 2

def main():
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
