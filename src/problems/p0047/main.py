# from tools import Primes
    
# def f(start=1000, seq_check=4):
    # primes = Primes(until=start)
    # cur = start
    # seq = seq_check
    # while seq > 0:
        # count = 0
        # for p in primes:
            # r = cur % p
            # if r == 0:
                # count += 1
            # if count == seq_check:
                # seq -= 1
                # break
        # else:
            # seq = seq_check
        # cur += 1
        # primes.get_more_primes(until=cur)
    # return cur - seq_check

def main(check=4):
    # Based on gen_primes algorithm in tools
    D = {}
    q = 2
    seq = check
    # Iterate until we find a sequence
    while seq > 0:
        if q not in D:
            # Failed sequence, revert count
            seq = check
            # Use sets instead of lists (removes duplicates)
            D[q*q] = set([q])
            # Need to include all witnesses (normally this is witnessed by 2)
            D.setdefault(q+q, set()).add(q)
        else:
            # Check for sequence
            if len(D[q]) >= check:
                # Success
                seq -= 1
            else:
                # Failure
                seq = check
            for p in D[q]:
                D.setdefault(p + q, set()).add(p)
            del D[q]
        q += 1
    return q - check
