from ...utils.primes import gen_primes

def rotate(s):
    return s[1:]+s[0]

def rotations_of(n):
    rotations = set()
    s = str(n)
    for i in range(len(s)-1):
        s = rotate(s)
        rotations.add(int(s))
    # Special case e.g. 11 (rotation is itself)
    if n in rotations: 
        rotations.remove(n)
    return rotations

def f(threshold):
    primes = set()
    gp = gen_primes()
    while True:
        prime = next(gp)
        if prime > threshold:
            break
        primes.add(prime)
    circular_primes = set()
    while len(primes) > 0:
        prime = primes.pop()
        circular = True
        potential_circulars = set([prime])
        for rotation in rotations_of(prime):
            if rotation in primes:
                primes.remove(rotation)
                potential_circulars.add(rotation)
            else:
                circular = False
                break
        if circular:
            circular_primes |= potential_circulars
    return len(circular_primes)

def main():
    return f(1000000)
