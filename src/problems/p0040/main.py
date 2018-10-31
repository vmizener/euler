# 1 2 3 4 5 6 7 8 9         # 9
# 10 11 12 ... 98 99        # 99-9 = 90
# 100 101 ... 998 999       # 999-99 = 900

# Number of N digit numbers = 9*10^(N-1)

# 9+90*2+900*3

def getDigit(d):
    ''' The digit will be the fractional part of some number.
        Find how many digits that number has. '''
    d -= 1        # The program counts from 0, so we adjust for that
    digits = 1    # How many digits is the current magnitude
    num = 9        # How many numbers with that many digits
    prev = 0    # The total number of digits from preceding magnitudes
    count = 9    # the total number of digits including the current magnitude
    while count < d:
        num *= 10
        digits += 1
        prev = count
        count += num*digits
    d -= prev
    r = (10**(digits-1))+int(d/digits)
    c = d%digits
    return int(str(r)[c])

def main():
    val = 1
    for i in range(7):
        val *= getDigit(10**i)
    return val
