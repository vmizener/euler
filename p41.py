from math import floor,sqrt
from itertools import permutations
from time import time
    
def isPrime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3,int(floor(sqrt(x))),2):
        if x % i == 0:
            return False
    return True
    
def g():
    s = '987654321'
    for i in range(len(s)):
        for p in permutations(s[i:]):
            el = int(''.join(p))
            if isPrime(el):
                return el
    return False
    
if __name__ == '__main__':
    start = time()
    print g()
    print "Time Elapsed: "
    print time()-start