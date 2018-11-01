def min_joint_strings(s1, s2):
    ret = set()
    if len(s2) == 0:
        return [s1]
    max_len = float('inf')
    for i in range(len(s1)+1):
        for entry in min_joint_strings(s1[i:], s2[1:]):
            if len(entry) == 0:
                option = s1[:i] + s2[0]
            elif entry[0] == s2[0]:
                option = s1[:i] + entry
            else:
                option = s1[:i] + s2[0] + entry
            if len(option) < max_len:
                ret = set([option])
                max_len = len(option)
            elif len(option) == max_len:
                ret.add(option)
    return ret

def compare_pools(pool1, pool2):
    op1, op2 = [next(iter(pool)) for pool in [pool1, pool2]]
    if len(op1) == len(op2):
        return set(pool1) | set(pool2)
    if len(op1) < len(op2):
        return pool1
    else:
        return pool2

def get_best_string_options_from_pool(lines):
    ret = min_joint_strings(lines[0], lines[1])
    for line in lines[2:]:
        ret_options = None
        for option in ret:
            pool_options = min_joint_strings(option, line)
            if not ret_options:
                ret_options = pool_options
            else:
                ret_options = compare_pools(ret_options, pool_options)
        ret = ret_options
    return ret, len(next(iter(ret)))

def main():
    with open('keylog.txt', 'r') as fh:
        lines = [line.strip() for line in fh.readlines()]
    ret, min_len = get_best_string_options_from_pool(lines)
    return {
        'Options': ret,
        'Min Len': min_len,
    }
