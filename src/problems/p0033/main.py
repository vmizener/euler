from fractions import gcd
from functools import reduce
from operator import mul

def is_digit_cancellable(n, d):
    if n != d:
        str_n = str(n)
        str_d = str(d)
        if '0' not in str_n + str_d:
            div = float(n)/float(d)
            for i in range(len(str_n)):
                for j in range(len(str_d)):
                    if str_n[i] == str_d[j]:
                        new_n = float(str_n[:i]+str_n[i+1:])
                        new_d = float(str_d[:j]+str_d[j+1:])
                        if new_n/new_d == div:
                            return True
    return False

def main():
    digit_cancellables = set()
    for n in range(10, 100):
        for d in range(n, 100):
            if is_digit_cancellable(n, d):
                digit_cancellables.add((n, d))
    pn, pd = tuple(map(lambda x: reduce(mul, x, 1), zip(*digit_cancellables)))
    return pd//gcd(pn, pd)
