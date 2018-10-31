from ...utils.primes import gen_primes

def main():
    g = gen_primes()
    sum = 0
    while True:
        r = next(g)
        if r >= 2000000:
            return sum
        sum += r
