from math import log

def main():
    with open('base_exp.txt', 'r') as fh:
        exponentials = [[int(item) for item in line.strip().split(',')] for line in fh]

    # Use logarithms
    # I am embarassed to say it took me way to long to think of that
    best_idx, best_val = None, None
    for idx, (next_base, next_exp) in enumerate(exponentials):
        next_val = next_exp * log(next_base)
        if not best_idx or next_val > best_val:
            best_idx, best_val = idx, next_val
    return best_idx+1
