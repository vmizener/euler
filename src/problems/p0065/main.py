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

def main():
    # We're just going to use the trick the problem gave us instead of calculating it ourselves
    # :(
    ret = []
    seq = [2]
    [seq.extend([1, 2*el, 1]) for el in range(1, 34)]
    print('cont frac:\n{}'.format(seq))
    num, dem = cont_frac_to_rational(seq)
    ret.append(('100th num', num))
    ret.append(('100th dem', dem))
    ret.append(('answer', sum([int(el) for el in list(str(num))])))
    return ret
