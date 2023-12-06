import re

input_file = "day-5/input.txt"

values = []
convert_rates = []

with open(input_file) as f:
    f = f.read()
    f = f.split(':')
    f = [re.sub(r'[^0-9\n\s]+', '', el) for el in f] # remove words
    f = [el.strip().split('\n') for el in f if el]

    input_value = f.pop(0)[0] # keep the initial values separated
    values = [int(v) for v in input_value.split() if v]
    # create new array:
    # [
    #   [[], []], # seed-to-soil
    #   [[]],     # soil-to-fert
    #   [[], [], []] # fert-to-water
    #   ecc
    # ]
    convert_rates = []
    for el in f:
        temp = []
        for s in el:
            numeri = [int(num) for num in s.split()]
            temp.append(numeri)
        convert_rates.append(temp)


def calculate_return(n: int, data: list) -> int:
    d, s, r = data
    if n >= s and n < s + r:
        return d + n - s
    return -1


def convert(i, v, data) -> None:
    for x in data:
        r = calculate_return(v, x)
        if r != -1: 
            # values[i] = r
            # break
            return r
    return v


for i, v in enumerate(values):
    current_v = v
    for j, rate in enumerate(convert_rates):
        current_v = convert(i, current_v, rate)
    values[i] = current_v
print(min(values))