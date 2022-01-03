import sys


DAYS = 80


def tick(value: int) -> int:
    if value == 0:
        return 6
    return value - 1


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    states = [int(x) for x in f.readline().rstrip().split(',')]
    for _ in range(0, DAYS):
        next_states = [8 for x in states if x == 0]
        states = [tick(x) for x in states]
        states.extend(next_states)

    print(len(states))
