from time import time

days_in_month = {
    1:  31,
    2:  28,
    3:  31,
    4:  30,
    5:  31,
    6:  30,
    7:  31,
    8:  31,
    9:  30,
    10: 31,
    11: 30,
    12: 31,
}

def is_leap(y):
    if (y/4.0).is_integer():
        if (y/100.0).is_integer():
            if (y/400.0).is_integer():
                return True
            return False
        return True
    return False

def next_first_of_month():
    cur_day = 1     # Monday
    cur_month = 1   # January
    cur_year = 1900 # 1900
    while True:
        yield cur_day, cur_year
        adder = days_in_month[cur_month]
        if cur_month == 2 and is_leap(cur_year):
            adder += 1
        cur_month += 1
        if cur_month == 13:
            cur_month = 1
            cur_year += 1
        cur_day = (cur_day + adder) % 7

def main():
    count = 0
    for day, year in next_first_of_month():
        if 1901 <= year <= 2000 and day == 0:
            count += 1
        elif year > 2000:
            break
    return count
