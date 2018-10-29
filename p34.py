from math import factorial
from time import time

def is_digit_factorial(n):
    return sum([factorial(int(d)) for d in str(n)]) == n

def f():
    ret = 0
    for i in range(10, 2540160): # max is 7*9!
        if is_digit_factorial(i):
            ret += i
    return ret
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s