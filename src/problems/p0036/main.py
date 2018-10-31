def is_palindrome(s):
    # Assumes string input
    ret = True
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            ret = False
            break
        else:
            i += 1
            j -= 1
    return ret

def main():
    total = 0
    for i in range(1, 1000000, 2):
        # Even numbers are guaranteed to have a trailing zero in base 2
        # (which would imply leading zeros for the palindrome, a no-no)
        # We cover base 10 trailing zeros as a bonus since 10 is also even
        if is_palindrome(str(i)) and is_palindrome(format(i, 'b')):
            total += i
    return total
