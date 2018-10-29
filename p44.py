from Queue import PriorityQueue
from math import sqrt
from time import time

def is_pentagonal(n):
    det = 1+24*n
    if det > 0:
        return (float(1+sqrt(det))/6).is_integer()
    return False
    
# def gen_pentagonals(n=1):
    # while True:
        # yield n*(3*n-1)/2.0, n
        # n += 1
    
# def f():
    # gp = gen_pentagonals()
    # pq = PriorityQueue()
    # last, last_i = gp.next()
    # while True:
        # next, next_i = gp.next()
        # D = next - last
        # pq.put((D, (last, next), (last_i, next_i)))
        # last, last_i = next, next_i
        # d, (pj, pk), (j, k) = pq.get_nowait()
        # while True:
            # if is_pentagonal(pk+pj) and is_pentagonal(d):
                # return d, j, k
            # nd = 3+(d+3*(k-j)*(k-j-1)/2)/(k-j)
            # pq.put((d+nd, (pj, pk+nd), (j, k+1)))
            # d, (pj, pk), (j, k) = pq.get_nowait()
            # if d > D+3:
                # pq.put((d, (pj, pk), (j, k)))
                # break
"""
Most people tried a brute force approach without proving optimality 
which is somewhat unsatisfactory. Here is an algorithm which also 
establishes optimality of the solution. We are looking for pentagon 
numbers P(n) and P(n+k) such that P(n)+P(n+k) and D=P(n+k)-P(n) are 
pentagon numbers, with D as small as possible. 

The crucial point now is the formula P(n+k)-P(n) = 3kn + P(k). Assuming 
D=P(m) we actually solve the equation P(m) = 3kn + P(k). In particular, k<m.
 
Hence the following algorithm works: 

For m=1,2,3,... and each 0<k<m we check if P(m)-P(k) is divisible by 3k. 
If so, then the quotient is n and we check if P(n+k)+P(n) is a pentagon 
number. If this is also the case, then we are done and D=P(m) yields the 
smallest difference. 

The algorithm has quadratic runtime in m. It took ~1 sec in Python.
"""
def p(n):
    return n*(3*n-1)/2.0
    
def f():
    m = 1
    while True:
        pm = p(m)
        for k in range(1, m):
            pk = p(k)
            q, r = divmod(pm-pk, 3*k)
            if r == 0 and is_pentagonal(p(q+k)+p(q)):
                return pm
        m += 1
                
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s