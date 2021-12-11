import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    horizontal = 0
    depth = 0

    for line in f:
        direction, value = line.split(' ')
        value = int(value)
        if direction == 'forward':
            horizontal += value
        elif direction == 'down':
            depth += value
        elif direction == 'up':
            depth -= value

    print(horizontal * depth)
