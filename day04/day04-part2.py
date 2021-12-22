import re
import sys


# First parameter to program is the input file
with open(sys.argv[1]) as f:
    draws = f.readline().rstrip().split(',')
    boards = list()

    # Set up the boards
    while line := f.readline():
        boards.append([
            set(),  # Column 1
            set(),  # Column 2
            set(),  # Column 3
            set(),  # Column 4
            set(),  # Column 5
        ])
        for i in range(0, 5):
            row = re.split(r'\s+', f.readline().strip())
            boards[-1].append(set(row))
            for j in range(0, 5):
                boards[-1][j].add(row[j])

    # Draw the numbers
    winners = set()
    last_winner_index = -1
    for draw in draws:
        for board_index in range(0, len(boards)):
            if board_index not in winners:
                for rowcol in boards[board_index]:
                    rowcol.discard(draw)
                    if len(rowcol) == 0:
                        winners.add(board_index)
                        last_winner_index = board_index
        if len(winners) == len(boards):
            print(int(draw) * sum(sum(int(x) for x in rowcol) for rowcol in boards[last_winner_index][:5]))
            break
