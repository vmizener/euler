def f(denoms, s):
    if len(denoms) == 1:
        # This works because we assume the last denomination is 1
        total = 1
    else:
        total = 0
        denom = denoms[0]
        dc = s // denom
        while dc >= 0:
            cursum = s - denom*dc
            total += f(denoms[1:], cursum)
            dc -= 1
    return total

def main():
    return f([200, 100, 50, 20, 10, 5, 2, 1], 200)
