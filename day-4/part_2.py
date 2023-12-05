
input_file = "day-4/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()


def check_card(line: str) -> int:
    numbers = line.split(':')[1]
    winning_n, c_numbers = numbers.split('|')
    winning_n = [int(n) for n in winning_n.split(' ') if n]
    c_numbers = [int(n) for n in c_numbers.split(' ') if n]
    count = 0
    for n in c_numbers:
        if n in winning_n: count += 1
    return count


mem = [1] * len(lines)

for i, line in enumerate(lines):
    n = check_card(line)
    for j in range(n):
        mem[i + j + 1] += mem[i]

print(sum(mem))