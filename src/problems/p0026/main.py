from time import time

def check(divisor):
    step = 1
    dividend = 1
    dividends = {}
    while True:
        dividends[dividend] = step
        expanded_dividend = dividend
        while expanded_dividend < divisor:
            expanded_dividend *= 10
        remainder = expanded_dividend % divisor
        if remainder == 0:
            return 0
        elif remainder in dividends:
            return step - dividends[remainder] + 1
        else:
            dividend = remainder
            step += 1

def main():
    divisor_range = 1000
    divisor, max_cycle = 0, 0
    for i in range(2, divisor_range):
        c = check(i)
        if c > max_cycle:
            divisor = i
            max_cycle = c
    return [
        ('d', divisor),
        ('cycle', max_cycle),
    ]
