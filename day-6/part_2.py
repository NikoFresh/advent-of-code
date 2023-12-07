import re

input_file = "day-6/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()

def parse_input(raw: str) -> list:
    f = [re.sub(r'\D', '', el) for el in raw]
    return f


def find_ways(race: list) -> int:
    tot = 0
    tot_time, space = int(race[0]), int(race[1])
    for speed in range(tot_time):
        time = tot_time - speed
        if speed * time > space: tot += 1
    return tot

race = parse_input(lines)

print(find_ways(race))