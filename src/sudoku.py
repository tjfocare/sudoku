import csv
import random
import sys

from datetime import datetime

import numpy as np

from board import Board, Cell, TYPE

from helpers import print_board, read_boards, get_grid

x = 0


def is_in_row(bo, num, row):
    return int(num) in bo.get_row(row)


def is_in_col(bo, num, col):
    return int(num) in bo.get_col(col)


def is_in_square(bo, num, row, col):
    mask = np.ones(9).reshape(3, 3)
    window = np.zeros(81).reshape(9, 9)
    square = []

    if row % 3 == 0 and col % 3 == 0:
        # top left
        window[row:row + 3, col:col + 3] = mask

    elif row % 3 == 0 and col % 3 == 1:
        # top middle
        window[row:row + 3, col - 1:col + 2] = mask

    elif row % 3 == 0 and col % 3 == 2:
        # top right
        window[row:row + 3, col - 2:col + 1] = mask

    elif row % 3 == 1 and col % 3 == 0:
        # middle left
        window[row - 1:row + 2, col:col + 3] = mask

    elif row % 3 == 1 and col % 3 == 1:
        # middle middle
        window[row - 1:row + 2, col - 1:col + 2] = mask

    elif row % 3 == 1 and col % 3 == 2:
        # middle right
        window[row - 1:row + 2, col - 2:col + 1] = mask

    elif row % 3 == 2 and col % 3 == 0:
        # bottom left
        window[row - 2:row + 1, col:col + 3] = mask

    elif row % 3 == 2 and col % 3 == 1:
        # bottom middle
        window[row - 2:row + 1, col - 1:col + 2] = mask

    elif row % 3 == 2 and col % 3 == 2:
        # bottom right
        window[row - 2:row + 1, col - 2:col + 1] = mask

    square = np.array(np.multiply(bo.get_grid(TYPE.ARRAY), window), int)

    return np.isin(num, square)


def is_valid_placement(bo, num, row, col):
    return ((not is_in_row(bo, num, row)) and
            (not is_in_col(bo, num, col)) and
            (not is_in_square(bo, num, row, col)))


def find_next_empty(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            # bo[i][j] is user-editable
            if bo.is_editable(i, j):
                return i, j
    return False


def solve_board(bo):
    next_empty = find_next_empty(bo)

    if not next_empty:
        print_board(bo)
        return True
    else:
        row, col = next_empty

    # try all numbers
    for testVal in range(1, 10):
        if is_valid_placement(bo, testVal, row, col):
            # update board with new valid value
            bo.set_cell(testVal, row, col)

            # check if board is solved
            if solve_board(bo):
                return True

            bo.set_cell(x, row, col)

    return False


def main():

    if len(sys.argv) > 1:
        board_no = int(sys.argv[1])
    else:
        board_no = random.randint(0, 49)

    print('puzzle no: ', board_no)

    boards = read_boards()
    grid = get_grid(boards, board_no)
    board = Board(grid)

    start_time = datetime.now()
    print_board(board)

    print('solving...')
    solve_board(board)

    end_time = datetime.now()
    time_diff = (end_time - start_time)  # .strftime('%H:%M:%S')
    print('Solved in ' + str(time_diff))


def write_results():
    global steps_taken

    boards = read_boards()

    with open('test_results' + str(datetime.now()) + '.csv', mode='w') as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(['Puzzle no.', 'Time to complete', 'No. of steps'])

        for no in range(0, 49):
            board_no = no
            grid = get_grid(boards, board_no)

            steps_taken = 0
            board = Board(grid)

            start_time = datetime.now()
            print('solving... puzzle: ', board_no)
            solve_board(board)

            end_time = datetime.now()
            time_diff = (end_time - start_time)

            csv_writer.writerow([board_no, str(time_diff), steps_taken])


main()
# write_results()
