import re

input_file = "day-3/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()


def check_str(s: str) -> bool:
    '''
    s: string to check

    return True if char is symbol
    '''
    for c in s:
        if c != '.' and not c.isnumeric():
            return True
    return False


def map_numbers(s: list) -> list[tuple[int, int, int]]:
    '''
    s: input to analize

    return List with tuple (n, x, y)
    '''
    out = []
    x = 0

    for y, line in enumerate(s):
        line = re.split(r'[^0-9]', line)
        for c in line:
            if c.isnumeric():
                out.append((int(c), x, y))
                x += len(c)
            x += 1
        x = 0

    
    return out

def is_valid_number(t: tuple, s: list) -> int:
    '''
    t: (n, x, y)
    s: input file

    return n if valid else 0
    '''
    n, x, y = t
    n_len = len(str(n))

    x_start = 0 if x == 0 else -1
    x_end = n_len - 1 if x == len(s[y]) else n_len
    y_start = 0 if y == 0 else -1
    y_end = 0 if y == len(s) - 1 else 1

    # put everything adjacent to the number in one string, then check
    s_temp = ''
    for y_t in range(y + y_start, y + y_end + 1):
        s_temp += s[y_t][x + x_start : x + x_end + 1]
    
    return n if check_str(s_temp) else 0


nlist = map_numbers(lines)

tot = 0
for n in nlist:
    tot += is_valid_number(n, lines)
    
print(tot)