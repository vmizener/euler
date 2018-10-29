from itertools import combinations, permutations
from operator import add
from time import time
from tools import Primes
    
def f():
    # Set used to keep track of what has already been tested
    D = set()
    # Collection used to check if a number is prime
    primes = Primes()
    # Set of results
    ret = set()
    # Iterate over all 4-digit numbers
    for i in xrange(1000, 10000):
        # Skip terms that have already been tested
        if i in D: continue
        # Build a set of unique integer permutations
        permutation_set = set(map(lambda x: int(reduce(add, x)), permutations(str(i))))
        # Add these permutations to D to avoid testing again
        D |= permutation_set
        # Filter for primes, then sort
        permutation_list = sorted(list(filter(lambda x: x in primes, permutation_set)))
        # Select a pair of elements (second is larger)
        for first, second in combinations(permutation_list, 2):
            # Generate an equidistant third element
            third = 2*second - first
            # Add the triplet if the third is also a permutation (and prime)
            if third in permutation_list:
                ret.add((first, second, third))
    # Filter for 4-digit triplets only (caused by leading zero permutations)
    ret = filter(lambda x: all(map(lambda y: len(str(y)) == 4, x)), ret)
    # Return the set of concatenated triplets
    return map(lambda x: reduce(add, map(lambda y: str(y), x)), ret)
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s