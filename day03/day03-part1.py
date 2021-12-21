import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    counts = [int(x) for x in f.readline().rstrip()]

    for line in f:
        counts = [x + y for x, y in zip(counts, [1 if int(x) else -1 for x in line.rstrip()])]

    gamma = int(''.join(['1' if x > 0 else '0' for x in counts]), base=2)
    epsilon = int(''.join(['0' if x > 0 else '1' for x in counts]), base=2)

    print(gamma * epsilon)
