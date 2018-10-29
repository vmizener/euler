from time import time

def main():
    return sum([int(c) for c in str(pow(2, 1000))])
    
if __name__ == '__main__':
    start = time()
    val = main()
    print "Value: ", val
    print "======="
    print "Time Elapsed : ", time()-start