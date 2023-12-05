import re

input_file = "day-3/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()


def check_numbers(s: str) -> bool:
    '''
    s: string to check

    return True if there are two numbers
    '''
    s = re.split(r'[^0-9]', s)
    count = []
    for el in s:
        if el.isnumeric(): count.append(int(el))
    
    return count

def map_gears(s: list) -> list[tuple[int, int, int]]:
    '''
    s: input to analize

    return List with tuple (x, y)
    '''
    out = []
    x = 0

    for y, line in enumerate(s):
        # line = re.split(r'[^0-9]', line)
        # line = line.split('')
        for c in line:
            if c == '*':
                out.append((x, y))
                x += len(c)
            x += 1
        x = 0
    
    return out

def is_valid_gear(g: tuple, s: list) -> int:
    '''
    g: (n, x, y)
    s: input file

    return n if valid else 0
    '''
    x, y = g
    
    x_start = 0 if x == 0 else -3
    x_end = 0 if x == len(s[y]) else 2
    y_start = 0 if y == 0 else -1
    y_end = 0 if y == len(s) - 1 else 1

    # put everything adjacent to the gear in one string, then check
    s_temp = ''
    for y_t in range(y + y_start, y + y_end + 1):
        s_temp += s[y_t][x + x_start : x + x_end + 1]
    
    # return n if check_numbers(s_temp) else 0
    valid_n = check_numbers(s_temp)
    out = valid_n[0] * valid_n[1] if len(valid_n) == 2 else 0
    return out



nlist = map_gears(lines)

tot = 0
for g in nlist:
    tot += is_valid_gear(g, lines)
    
print(tot)