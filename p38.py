def isPanDigital(x):
    if ('0' in x) or (len(x) == len(set(x))):
        return False
    return True
            
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
    
def f():
    pool = list(str(987654321))
    largest = 0
    r = ""
    for i in range(1,5):
        for el in permute(pool, i):
            for j in range(1,6):
                val = sumrange(el,j)
                if isPanDigital(str(val)):
                    if val > largest:
                        largest = val
                        r = el
    print largest
    print r
    
if __name__ == '__main__':
    f()
