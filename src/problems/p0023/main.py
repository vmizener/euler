from time import time
from ...utils.primes import gen_divisors

def is_abundant(n):
    s = sum(list(gen_divisors(n))[:-1])
    return s > n

def main():
    ret = 0
    abundants = []
    for i in range(1, 28123):
        sum_of_two_abundants = False
        for abundant in abundants:
            if abundant > i/2:
                break
            if (i - abundant) in abundants:
                sum_of_two_abundants = True
                break
        if not sum_of_two_abundants:
            ret += i
        if is_abundant(i):
            abundants.append(i)
    return ret
