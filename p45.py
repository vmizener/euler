from time import time

def T(n):
    return n*(n+1)/2
    
def P(n):
    return n*(3*n-1)/2

def H(n):
    return n*(2*n-1)

def f():
    t = 286
    Tt = T(t)
    p = 166
    Pp = P(p)
    h = 144
    Hh = H(h)
    while True:
        if Tt < Hh:
            t += 1
            Tt = T(t)
            continue
        elif Tt == Hh:
            if Pp < Hh:
                p += 1
                Pp = P(p)
                continue
            elif Pp == Hh:
                return (Tt, Pp, Hh), (t, p, h)
        h += 1
        Hh = H(h)

if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s, 'seconds'