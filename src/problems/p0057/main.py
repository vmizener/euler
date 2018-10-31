from fractions import Fraction as frac

def main(count=1000):
    ret = 0
    cur = frac(1,2)
    for _ in range(count):
        check = cur+1
        if len(str(check.numerator)) > len(str(check.denominator)):
            ret += 1
        cur = invert(2+cur)

    return ret

def invert(x):
    return frac(x.denominator, x.numerator)
