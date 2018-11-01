def gen_fib():
    a, b = 0, 1
    while True:
        ret = a + b
        a, b = b, ret
        yield ret

def main():
    ret = 0
    fib = gen_fib()
    next_fib = next(fib)
    while next_fib < 4000000:
        if next_fib % 2 == 0:
            ret += next_fib
        next_fib = next(fib)
    return ret

# Wow this solution is baller as hell (though actually slower lol)
"""
def main():
    # Steps between each even fib is phi^3 (phi is step between each fib, every 3rd is even)
    step = lambda x: round(x*4.236068)
    last = 2
    ret = 0
    while last < 4000000:
        ret += last
        last = step(last)
    return ret
"""
