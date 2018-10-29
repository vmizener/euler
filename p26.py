from sys import argv
from time import time

def check(divisor):
    step = 1
    dividend = 1
    dividends = {}
    while True:
        dividends[dividend] = step
        expanded_dividend = dividend
        while expanded_dividend < divisor:
            expanded_dividend *= 10
        remainder = expanded_dividend % divisor
        if remainder == 0:
            return 0
        elif remainder in dividends:
            return step - dividends[remainder] + 1
        else:
            dividend = remainder
            step += 1
        
def f(divisor_range):
    divisor, max_cycle = 0, 0
    for i in range(2, divisor_range):
        c = check(i)
        if c > max_cycle:
            divisor = i
            max_cycle = c
    return divisor, max_cycle
    
if __name__ == '__main__':
    s = time()
    if len(argv) > 1:
        print f(*map(int, argv[1:]))
    else:
        print f(1000)
    print 'elapsed:', time()-s