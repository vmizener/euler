from ...utils.primes import gen_divisors

def is_1_to_9_pandigital(s):
    return '0' not in s and 9 == len(s) == len(set(s))

def identify_1_to_9_pandigital_products(n):
    ret = set()
    divisors = set(gen_divisors(n))
    for divisor in divisors:
        digits = str(divisor) + str(n//divisor) + str(n)
        if is_1_to_9_pandigital(digits):
            ret.add(n)
    return ret

def main():
    pandigital_products = set()
    for i in range(4000, 10000):
        pandigital_products |= identify_1_to_9_pandigital_products(i)
    return sum(pandigital_products)
