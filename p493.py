from math import factorial
from time import time
    
def nCr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))
    
def f():
    return
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s