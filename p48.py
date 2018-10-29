def selfpower(x,truncate=10000000000):
    pow = x
    val = x
    alt = 1
    while (pow > 1):
        if (pow%2==0):
            val = val**2
            pow = pow/2
            val %= truncate
        else:
            alt = alt*val
            pow = pow-1
            alt %= truncate
    return (val*alt)%truncate

def f():
    truncate = 10000000000
    runningsum = 0
    for i in range(1001):
        runningsum += selfpower(i,truncate)
        runningsum %= truncate
    print runningsum
    
if __name__ == '__main__':
    f()