import re

input_file = "day-6/input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()

def parse_input(raw: str) -> list:
    f = [re.sub(r'[^0-9\n\s]+', '', el).strip() for el in raw]
    f = [el.split() for el in f]
    return list(zip(f[0], f[1]))


def find_ways(race: list) -> int:
    tot = 0
    tot_time, space = int(race[0]), int(race[1])
    for speed in range(tot_time):
        time = tot_time - speed
        if speed * time > space: tot += 1
    return tot

races = parse_input(lines)
out = 1
for race in races:
    out *= find_ways(race)

print(out)