import sys
from typing import Dict


DAYS = 256


def get_next_states(state_dict: Dict[int, int]) -> Dict[int, int]:
    result: Dict[int, int] = {
        8: state_dict[0]
    }
    for i in range(0, 8):
        result[i] = state_dict[i + 1]
    result[6] += state_dict[0]

    return result


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    states = {x: 0 for x in range(0, 9)}
    for x in f.readline().rstrip().split(','):
        states[int(x)] += 1
    for _ in range(0, DAYS):
        states = get_next_states(states)

    print(sum(states.values()))
