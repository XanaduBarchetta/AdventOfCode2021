import re
import sys


VALUE_REGEX = re.compile(r'\d+')


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    coords = dict()
    for line in f:
        x1, y1, x2, y2 = [int(value) for value in VALUE_REGEX.findall(line)]
        if x1 == x2:
            if y1 == y2:
                # Cover this unlikely case that the line is actually a point
                coords[(x1, y1)] = coords.get((x1, y1), 0) + 1
            else:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    coords[(x1, y)] = coords.get((x1, y), 0) + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                coords[(x, y1)] = coords.get((x, y1), 0) + 1

    print(sum(1 for count in coords.values() if count >= 2))
