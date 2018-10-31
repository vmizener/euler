from functools import reduce

def isPanDigital(s):
    return '0' not in s and 9 == len(s) == len(set(s))

def permute(pool, n, prefix=""):
    if len(pool) == 0 or n < 1:
        return [prefix]
    res = []
    for i in range(len(pool)):
        el = pool[i]
        p = pool[0:i]+pool[i+1:len(pool)]
        res += permute(p, n-1, prefix+el)
    return res

def sumrange(x, n):
    return reduce(lambda x,y: x+y, [str(int(x)*i) for i in range(1,n+1)])

def main():
    pool = list(str(987654321))
    largest = '0'
    r = ""
    for i in range(1,5):
        for el in permute(pool, i):
            for j in range(1,6):
                val = sumrange(el,j)
                if isPanDigital(str(val)):
                    if int(val) > int(largest):
                        largest = val
                        r = el
    return [
        ('largest product', largest),
        ('base integer', r),
    ]
