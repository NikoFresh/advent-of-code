input_file = "day-1/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()

#########

def part_one() -> int:
    out: int = 0
    for key in lines:
        num = [n for n in key if n.isnumeric()]
        out += int(f'{num[0]}{num[-1]}')
    return out


def part_two() -> int:
    numbers: list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    out: int = 0
    for key in lines:
        # save index of numbers
        # string
        num: list = []
        for i, c in enumerate(key):
            if c.isnumeric():
                num.append(c)
            else:
                for d, val in enumerate(numbers):
                    if key[i:].startswith(val):
                        num.append(d)


        out += int(f'{num[0]}{num[-1]}')
    return out

print(part_two())

