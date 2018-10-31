def main():
    i = '10'
    while True:
        val = int(i)
        if set(str(2*val)) == set(str(3*val)) \
                           == set(str(4*val)) \
                           == set(str(5*val)) \
                           == set(str(6*val)):
            break
        else:
            tail = i[1:]
            tailval = int(tail)+1
            if tailval > 6*int('1'*len(tail)):
                i = '1' + '0'*(len(tail)+1)
            else:
                i = '1' + str(tailval).zfill(len(tail))
    return val
