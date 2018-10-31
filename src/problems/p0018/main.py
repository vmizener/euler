from time import time

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def get_map(block_string):
    tmp = block_string.strip().split('\n')
    ret = []
    for line in tmp:
        ret.append(line.split(' '))
    return ret

def get_map_entry(n, m):
    x, y = n
    return int(m[x][y])

def get_neighbors(n, max_height):
    x, y = n
    if x == max_height:
        return []
    return [(x+1, y), (x+1, y+1)]

def main(triangle=triangle):
    d = {}
    map = get_map(triangle)
    h = len(map)-1
    for line_num, line in enumerate(map):
        for entry_num, entry in enumerate(line):
            node = (line_num, entry_num)
            d[node] = 0
    visit_queue = [(0,0)]
    cur = visit_queue[0]
    d[cur] = get_map_entry(cur, map)
    visited = set()
    while len(visit_queue) > 0:
        cur = visit_queue[0]
        visit_queue.pop(0)
        if cur in visited:
            continue
        visited.add(cur)
        neighbors = get_neighbors(cur, h)
        for neighbor in neighbors:
            d[neighbor] = max(d[neighbor],
                              d[cur] + get_map_entry(neighbor, map))
            visit_queue.append(neighbor)
    max_path = 0
    for y, x in enumerate([h]*h):
        max_path = max(d[(x,y)], max_path)
    return max_path
