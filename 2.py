import re

input_file = "input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()

def analize(line: str) -> (int, int):
    valid: bool = True
    red: int = 0
    blue: int = 0
    green: int = 0

    game, line = line.split(':')

    # - get game number
    game: int = int(re.findall(r'\d+', game)[0])

    # - separate each color
    colors = re.split('; |,', line)
    for color in colors:
        value = int(re.findall(r'\d+', color)[0]) # amount
        c = color.split()[-1] # color
        if c == 'red' and value > red: red = value
        if c == 'green' and value > green: green = value
        if c == 'blue' and value > blue: blue = value
    
    if red > 12 or green > 13 or blue > 14:
        valid = False

    power = red * green * blue
    return int(game) if valid else 0, power

out_game = 0
out_power = 0
for line in lines:
    game, power = analize(line)
    out_game += game
    out_power += power

print(out_game, out_power)