def get_prime_factors(n):
    """
    Get all the prime factors of [n]
    
    Returns dictionary (factors are keys, multiplicities are values)
    """
    pf = {}
    primes = gen_primes()
    while n > 1:
        p = primes.next()
        m = 0
        while m == 0:
            d, m = divmod(n, p)
            if m == 0:
                pf[p] = pf.setdefault(p, 0) + 1
                n = d
    return pf

def gen_divisors(n):
    """
    Generate all unique divisors of [n]
    """
    if n < 2:
        yield 1
        return
    factors_dict = get_prime_factors(n)
    factors = list(zip(factors_dict.keys(), factors_dict.values()))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return
    
def gen_primes():
    """ 
    Sieve of Eratosthenes
    Generator over indefinite range
    
    Warning:
    Ridiculously clever code ahead
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    D = {}
    
    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
            
        q += 1

class Primes(object):
    """
    Just a bunch of prime numbers.
    
    Use it to check if a given number is prime, but with an
    intelligently growing set you get to keep!
    
    e.g.
        >>> p = Primes()
        >>> 61 in p  # Eh speed
        True
        >>> 60 in p  # Fast
        False
        >>> 53 in p  # Faster!
        True
    """
    def __init__(self, until=0):
        self.__gp = gen_primes()
        self.primes = set()
        self.get_more_primes(until=until)
        
    def __iter__(self):
        for p in self.primes:
            yield p
        
    def __contains__(self, item):
        if item > self.last:
            self.get_more_primes(until=item)
        return item in self.primes
        
    def get_more_primes(self, until=0):
        self.last = self.__gp.next()
        self.primes.add(self.last)
        while self.last < until:
            self.last = self.__gp.next()
            self.primes.add(self.last)
        
if __name__ == '__main__':
    # Remove all .pyc files in current directory
    import os
    for f in os.listdir(os.curdir):
        if f.endswith('.pyc'):
            os.remove(f)
    