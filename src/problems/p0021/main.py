from time import time
from ...utils.primes import gen_divisors, gen_primes

def d(n):
    return sum(list(gen_divisors(n))[:-1])

def main():
    max = 10000
    cur = 2
    set = {}
    amicable = []
    for p in gen_primes():
        for n in range(cur, p):
            if n >= max:
                break
            dn = d(n)
            if n == dn:
                continue
            set[n] = dn
            if dn in set:
                if set[dn] == n:
                    amicable += [n, dn]
        cur = p+1
        if cur >= max:
            break
    return sum(amicable)
