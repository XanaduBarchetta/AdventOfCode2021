import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    result = 0
    previous = int(f.readline())

    for line in f:
        if int(line) > previous:
            result += 1
        previous = int(line)

    print(result)
