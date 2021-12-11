import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    horizontal = 0
    depth = 0
    aim = 0

    for line in f:
        direction, value = line.split(' ')
        value = int(value)
        if direction == 'forward':
            horizontal += value
            depth += (aim * value)
        elif direction == 'down':
            aim += value
        elif direction == 'up':
            aim -= value

    print(horizontal * depth)
