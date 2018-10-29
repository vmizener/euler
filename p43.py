from itertools import permutations
from operator import add
from time import time
    
def f():
    s = 0
    for pandigital_tup in permutations(['0','1','2','3','4','5','6','7','8','9']):
        pandigital = reduce(add, pandigital_tup)
        if int(pandigital[7:10]) % 17 == 0 \
                and int(pandigital[6:9]) % 13 == 0 \
                and int(pandigital[5:8]) % 11 == 0 \
                and int(pandigital[4:7]) % 7 == 0 \
                and int(pandigital[3:6]) % 5 == 0 \
                and int(pandigital[2:5]) % 3 == 0 \
                and int(pandigital[1:4]) % 2 == 0:
            s += int(pandigital)
    return s
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s