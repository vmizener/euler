from math import sqrt
from time import time
    
def is_square(n):
    return sqrt(n).is_integer()
    
def f():
    maxx, maxd = 0, 0
    for D in range(2, 8):
        D = float(D)
        if is_square(D):
            continue
        i = 1
        y = 1
        while True:
            iD = i*D
            x1, x2 = iD-1, iD+1
            # Sadness
    return maxx, maxd
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s