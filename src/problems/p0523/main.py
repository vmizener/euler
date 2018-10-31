def swap_sort(lst):
    steps = 0
    i = 0
    while i < len(lst)-1:
        if lst[i] > lst[i+1]:
            print(lst, (lst[i], lst[i+1]), swap_count(lst))
            lst = [lst[i+1]] + lst[:i+1] + lst[i+2:]
            i = 0
            steps += 1
        else:
            i += 1
    return steps, lst

def swap_count(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] != i+1:
            count += abs(lst[i] - i - 1)
    return count

def main():
    return swap_sort(list(range(1, 31)))
