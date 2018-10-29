from tools import gen_primes
from time import time

def f():
    g = gen_primes()
    sum = 0
    while True:
        r = g.next()
        if r >= 2000000:
            return sum
        sum += r

if __name__ == '__main__':
    start = time()
    print f()
    print "Time Elapsed: ", time()-start