def T(n):
    return n*(n+1)/2

def P(n):
    return n*(3*n-1)/2

def H(n):
    return n*(2*n-1)

def main():
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
                return [
                    ('Answer', Tt),
                    ('T_i', t),
                    ('P_i', p),
                    ('H_i', h),
                ]
        h += 1
        Hh = H(h)
