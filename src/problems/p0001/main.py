def sum_seq(n):
    return (n*(n+1))//2

def main():
    #return sum([n*sum_seq(999//abs(n)) for n in [3, 5, -15]])
    return 3*sum_seq(999//3) + 5*sum_seq(999//5) - 15*sum_seq(999//15)
