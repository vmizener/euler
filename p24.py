# x! ways to organize x elements

# 1,000,000th permutation of 10 elements
# Check if 1,000,000 >= 10!
# -> 10! = 3,628,800 < 1,000,000

# Elements remaining: {0,1,2,3,4,5,6,7,8,9}
# Length is non-zero (10)
# Permutation to find: 1,000,000
# 9! is 362,880 < 1,000,000
# 9!*2 is 725,760 < 1,000,000
# 9!*3 is 1,088,640 > 1,000,000
# First digit is 3rd element (2)

# Elements remaining: {0,1,3,4,5,6,7,8,9}
# Length is non-zero (9)
# Permutation to find: 1,000,000 - 725,760 = 274,240
# 8! is 40,320 < 274,240
# 8!*6 is 241,920 < 274,240
# 8!*7 is 282,240 > 274,240
# Second digit is 7th element (7)

# Elements remaining: {0,1,3,4,5,6,8,9}
# Length is non-zero (8)
# Permutation to find: 274,240 - 241,920 = 32320
# 7! is 5,040 < 32,320
# 7!*6 is 30,240 < 32,320
# 7!*7 is 35,280 > 32,320
# Third digit is 7th element (8)

# Elements remaining: {0,1,3,4,5,6,9}
# Length is non-zero (7)
# Permutation to find: 32,320 - 30,240 = 2,080
# 6! is 720 < 2,080
# 6!*2 is 1,440 < 2,080
# 6!*3 is 2,160 > 2,080
# Forth digit is 3rd element (3)

# Elements remaining: {0,1,4,5,6,9}
# Length is non-zero (6)
# Permutation to find: 2,080 - 1,440 = 640
# 5! is 120 < 640
# 5!*5 is 600 < 640
# 5!*6 is 720 > 640
# Fifth digit is 6th element (9)

# Elements remaining: {0,1,4,5,6}
# Length is non-zero (5)
# Permutation to find: 640 - 600 = 40
# 4! is 24 < 40
# 4!*2 is 48 > 40
# Sixth digit is 2nd element (1)

# Elements remaining: {0,4,5,6}
# Length is non-zero (4)
# Permutation to find: 40 - 24 = 16
# 3! is 6 < 16
# 3!*2 is 12 < 16
# 3!*3 is 18 > 16
# Seventh digit is 3rd element (5)

# Elements remaining: {0,4,6}
# Length is non-zero (3)
# Permutation to find: 16 - 12 = 4
# 2! is 2 < 4
# 2!*2 is 4 = 4
# Eighth digit is 2nd element (4)

# Elements remaining: {0,6}
# Length is non-zero (2)
# Permutation to find: 4 - 4 = 0
# No more permutations necessary; it is the final permutation (reversed list)
# Ninth digit is 6
# Tenth digit is 0

# The result is 2783915460

from math import factorial as fact
from sys import argv

def f(n, m):
    # nth lexicographic permutation of m elements (0 to m-1)
    if n == fact(m):
        return "".join(map(str,range(m-1,-1,-1)))
    else:
        return "".join(map(str,g(n, m, range(m))))
    
def g(n, m, els):
    if len(els) == 0:
        return []
    if n == fact(m-1) or n == 0:
        val = els.pop(0)
        els.reverse()
        return [val]+els
    r = 1
    while n > fact(m-1)*r:
        r += 1
    val = els.pop(r-1)
    return [val]+g(n-fact(m-1)*(r-1), m-1, els)
    
def main():
    try:
        n = int(argv[1])
    except:
        print "Input is of form [(int) nth permutation, (int) number of elements]"
        return
    try:
        m = int(argv[2])
    except:
        print "Input is of form [(int) nth permutation, (int) number of elements]"
        return
    if n > fact(m):
        print "N exceeds number of permutations; max is M! (%d here)" % fact(m)
        return
    print f(n,m)
    
if __name__ == '__main__':
    main()