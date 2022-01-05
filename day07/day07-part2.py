import sys
from typing import Dict


def get_nth_triangle(n: int):
    return int((n * n + n) / 2)


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

    """
    For this solution, we start with the rounded mean and work in a hill-climber fashion toward the solution
    """
    mean = total / number_of_values

    starting_position = round(mean)
    starting_positions = (starting_position - 1, starting_position, starting_position + 1)
    starting_fuels = [sum(get_nth_triangle(abs(candidate_position - position)) * count
                      for position, count in positions.items()) for candidate_position in starting_positions]
    direction = -1 if starting_fuels[0] < starting_fuels[1] else 1
    optimal_position = starting_position + direction
    total_fuel = starting_fuels[1]
    new_fuel = sum(get_nth_triangle(abs(optimal_position - position)) * count for position, count in positions.items())
    while new_fuel < total_fuel:
        total_fuel = new_fuel
        optimal_position += direction
        new_fuel = sum(get_nth_triangle(abs(optimal_position - position)) * count
                       for position, count in positions.items())

    print(total_fuel)
