from ...utils.primes import get_prime_factors

def main():
    x = 600851475143
    return max(get_prime_factors(x).keys())
