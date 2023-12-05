
input_file = "day-4/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()

def card_value(line: str) -> int:
    card, numbers = line.split(':')
    # card_number = card.split(' ')[-1]
    winning_n, c_numbers = numbers.split('|')
    winning_n = [int(n) for n in winning_n.split(' ') if n]
    c_numbers = [int(n) for n in c_numbers.split(' ') if n]
    count = -1
    for n in c_numbers:
        if n in winning_n: count += 1
    return pow(2, count) if count != -1 else 0

tot = 0
for line in lines:
    tot += card_value(line)

print(tot)