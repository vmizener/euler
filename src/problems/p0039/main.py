def main():
    max, pmax = 0, 0
    for p in range(2, 1000, 2):
        # Note that we only need to check even perimeters
        # (1) a**2 + b**2 == c**2 yields
        #    a    b    c    p
        # even even even even
        # even  odd  odd even
        #  odd even  odd even
        #  odd  odd even even
        count = 0
        for a in range(1, p):
            # (2) a + b + c == p  ->  c == p - a - b
            # Substituting (2) into (1), we reduce to find
            # (3) b = p*(p-2*a)/(2*(p-a))
            b, r = divmod(p*(p-2*a),(2*(p-a)))
            if a > b:
                # Iterate over each value of a until a > b 
                # (as then it will repeat pairs)
                break
            elif r == 0:
                # Of course, count integral solutions
                count += 1
        if count > max:
            max, pmax = count, p
    return pmax
