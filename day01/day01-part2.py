import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    result = 0

    readings = f.readlines()
    # Obtain the sums for all 3-value reading windows
    sums = [sum(int(x) for x in readings[i:i+3]) for i in range(0, len(readings)-2)]

    previous = sums[0]
    for value in sums[1:]:
        if value > previous:
            result += 1
        previous = value

    print(result)
