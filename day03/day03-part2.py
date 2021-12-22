import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    o2 = list()
    co2 = list()

    for line in f:
        o2.append(line.rstrip())
        co2.append(line.rstrip())

    # Assert True: o2 and co2 are identical lists of string representations of base2 integers

    # Process bit criteria for o2
    index = 0
    while len(o2) > 1:
        ones = [x for x in o2 if x[index] == '1']
        zeroes = [x for x in o2 if x[index] == '0']
        index += 1
        o2 = ones if len(ones) >= len(zeroes) else zeroes

    # Process bit criteria for co2
    index = 0
    while len(co2) > 1:
        ones = [x for x in co2 if x[index] == '1']
        zeroes = [x for x in co2 if x[index] == '0']
        index += 1
        co2 = ones if len(ones) < len(zeroes) else zeroes

    print(int(o2[0], base=2) * int(co2[0], base=2))
