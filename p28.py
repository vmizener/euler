from sys import argv
from time import time

def f(dim):
    # Takes only positive, odd integers!
    if dim == 1:
        return 1
    else:
        c = (dim)**2
        return sum([c-(dim-1)*i for i in range(4)]) + f(dim-2)
    
if __name__ == '__main__':
    s = time()
    if len(argv) > 1:
        print f(*map(int, argv[1:]))
    else:
        print f(1001)
    print 'elapsed:', time()-s