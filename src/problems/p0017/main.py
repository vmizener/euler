from time import time

def main():
    ret = 0
    for i in range(1000):
        ret += len(int_to_english(str(i+1)))
    return ret

VAL = {1: 'One',
       2: 'Two',
       3: 'Three',
       4: 'Four',
       5: 'Five',
       6: 'Six',
       7: 'Seven',
       8: 'Eight',
       9: 'Nine',

       10: 'Ten',
       11: 'Eleven',
       12: 'Twelve',
       13: 'Thirteen',
       14: 'Fourteen',
       15: 'Fifteen',
       16: 'Sixteen',
       17: 'Seventeen',
       18: 'Eighteen',
       19: 'Nineteen',

       20: 'Twenty',
       30: 'Thirty',
       40: 'Forty',
       50: 'Fifty',
       60: 'Sixty',
       70: 'Seventy',
       80: 'Eighty',
       90: 'Ninety'}

def int_to_english(s):
    ret = ''
    if int(s) == 1000:
        ret = 'OneThousand'
    elif int(s) >= 100:
        ret += VAL[int(s[0])]
        ret += 'Hundred'
        s = s[1:]
        if int(s) != 0:
            ret += 'And'
            ret += int_to_english(s)
    elif int(s) >= 20:
        ret += VAL[int(s[0]+'0')]
        s = s[1:]
        if int(s) != 0:
            ret += int_to_english(s)
    else:
        ret = VAL[int(s)]
    return ret
