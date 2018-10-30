#!/usr/bin/env python3
from math import floor, e

def cont_frac_to_rational(cont_frac_seq):
    # https://en.wikipedia.org/wiki/Continued_fraction#Infinite_continued_fractions_and_convergents
    h, k = [0, 1], [1, 0]
    for el in cont_frac_seq:
        h[0], h[1] = h[1], el*h[1]+h[0]
        k[0], k[1] = k[1], el*k[1]+k[0]
    return h[-1], k[-1]

def gen_cont_frac(val, iter_count=10):
    """
    !!DON'T USE!!
    Inaccurate after about 20 iterations!!
    """
    ret = []
    for _ in range(iter_count):
        ret.append(int(floor(val)))
        print(len(ret), ret)
        val = 1/(val - ret[-1])  # DANGER ZONE
    return ret

if __name__ == '__main__':
    # We're just going to use the trick the problem gave us instead of calculating it ourselves
    # :(
    seq = [2]
    [seq.extend([1, 2*el, 1]) for el in range(1, 34)]
    print(len(seq), seq)
    num, dem = cont_frac_to_rational(seq)
    print(num, dem)
    print(sum([int(el) for el in list(str(num))]))
