from time import time

def is_digit_nth_power(x, n):
    s = str(x)
    return x == sum([int(c)**n for c in s])
    
def f():
    digit_nth_powers = set()
    for i in range(10, 354294):
        if is_digit_nth_power(i, 5):
            digit_nth_powers.add(i)
    return sum(digit_nth_powers)
    
if __name__ == '__main__':
    s = time()
    print f()
    print 'elapsed:', time()-s