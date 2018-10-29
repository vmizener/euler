from time import time

VALSET = {1: 1}

def main():
    maxseq = 0
    start = None
    for i in range(1, 1000000):
        seqlen = collatz(i)
        if seqlen > maxseq:
            maxseq = seqlen
            start = i
    return maxseq, start
    
def collatz(cur):
    if cur in VALSET:
        return VALSET[cur]
    else:
        if cur%2 == 0:
            val = collatz(cur/2) + 1
        else:
            val = collatz(3*cur+1) + 1
        VALSET[cur] = val
        return val

if __name__ == '__main__':
    start = time()
    seq, start = main()
    print "Maximum Sequence :", seq
    print ".... Starting at :", start
    print "=================="
    print "... Time Elapsed : ", time()-start