import sys
from typing import Dict


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    positions: Dict[int, int] = dict()
    total = 0
    number_of_values = 0
    highest_count = 0
    for x in f.readline().rstrip().split(','):
        value = int(x)
        positions[value] = positions.get(value, 0) + 1
        if positions[value] > highest_count:
            highest_count = positions[value]
        total += value
        number_of_values += 1

    mean = total / number_of_values
    candidate_positions = [position for position, count in positions.items() if count == highest_count]
    optimal_position = min(candidate_positions, key=lambda position: abs(position - mean))
    total_fuel = sum(abs(optimal_position - position) * count for position, count in positions.items())
    new_fuel = 0
    difference = 1
    sign = 1
    if optimal_position > mean:
        sign = -1
    new_fuel = sum(abs((optimal_position + (sign * difference)) - position) * count
                   for position, count in positions.items())
    while new_fuel < total_fuel:
        total_fuel = new_fuel
        difference += 1
        new_fuel = sum(abs((optimal_position + (sign * difference)) - position) * count
                       for position, count in positions.items())

    print(total_fuel)
