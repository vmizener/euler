from time import time
from tools import Primes

def f():
    primes = Primes(until=11)
    ret = set()
    while len(ret) < 11:
        prime = primes.last
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) not in primes or \
                    int(str_prime[:-i]) not in primes:
                break
        else:
            ret.add(prime)
        primes.get_more_primes()
    return sum(ret)
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s