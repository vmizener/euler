from time import time
from tools import Primes

def calc(n, a, b):
    return n*n + a*n + b
    
def check_prime_sequence(a, b, primes):
    ret = 0
    val = calc(ret, a, b)
    while val in primes:
        ret += 1
        val = calc(ret, a, b)      
    return ret
    
def f():
    max = 0
    p = Primes()
    ret = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            l = check_prime_sequence(a, b, p)
            if l > max:
                max = l
                ret = a*b
    return ret

if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s