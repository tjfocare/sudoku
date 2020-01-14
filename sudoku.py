import re

import warnings

import numpy as np

warnings.simplefilter(action='ignore', category=FutureWarning)

x = 0

# boards = open('./sudoku.txt', 'r')

boards = np.array([[]])

test = open('./sudoku.txt', 'r').readlines()

for line in test:
    if (re.match('[A-Za-z]+\s[0-9]*', line)):
        # print(line)
        var = []
    else:
        if (re.match('[\n]', line[-1])):
            grid_row = list(line)[:-1]
        else:
            grid_row = list(line)
        boards = np.append(boards, grid_row)

boards = np.reshape(boards, (-1, 9))

board = boards[0:9, :]

# board = np.array([
#     [x, x, x, x, x, x, x, x, x],
#     [x, 8, 9, 1, 2, x, 4, 5, 6],
#     [4, 5, 6, 7, 8, 9, 1, 2, 3],
#     [3, 1, 2, 8, 4, 5, 9, 6, 7],
#     [6, 9, 7, 3, 1, x, 8, 4, 5],
#     [8, 4, 5, 6, 9, 7, 3, 1, 2],
#     [2, 3, 1, 5, 7, x, 6, 9, 8],
#     [9, 6, 8, 2, 3, 1, 5, 7, 4],
#     [5, 7, 4, 9, 6, 8, 2, 3, x],
# ])


def is_empty(bo, row, col):
    return bo[row][col] == x


def is_in_row(bo, num, row):
    return np.isin(num, bo[row])


def is_in_col(bo, num, col):
    return num in bo[:, col]


def is_in_square(bo, num, row, col):

    mask = np.ones(9).reshape(3, 3)
    window = np.zeros(81).reshape(9, 9)
    square = []

    if (row % 3 == 0 and col % 3 == 0):
        # top left
        window[row:row + 3, col:col + 3] = mask

    elif (row % 3 == 0 and col % 3 == 1):
        # top middle
        window[row:row + 3, col - 1:col + 2] = mask

    elif (row % 3 == 0 and col % 3 == 2):
        # top right
        window[row:row + 3, col - 2:col + 1] = mask

    elif (row % 3 == 1 and col % 3 == 0):
        # middle left
        window[row - 1:row + 2, col:col + 3] = mask

    elif (row % 3 == 1 and col % 3 == 1):
        # middle middle
        window[row - 1:row + 2, col - 1:col + 2] = mask

    elif (row % 3 == 1 and col % 3 == 2):
        # middle right
        window[row - 1:row + 2, col - 2:col + 1] = mask

    elif (row % 3 == 2 and col % 3 == 0):
        # bottom left
        window[row - 2:row + 1, col:col + 3] = mask

    elif (row % 3 == 2 and col % 3 == 1):
        # bottom middle
        window[row - 2:row + 1, col - 1:col + 2] = mask

    elif (row % 3 == 2 and col % 3 == 2):
        # bottom right
        window[row - 2:row + 1, col - 2:col + 1] = mask

    square = np.array(np.multiply(bo, window), int)

    return np.isin(num, square)


def is_valid(bo, num, row, col):
    return ((not is_in_row(bo, num, row)) and
            (not is_in_col(bo, num, col)) and
            (not is_in_square(bo, num, row, col)))


def find_next_empty(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            if (is_empty(bo, i, j)):
                return (i, j)
    return False


def solve_board(bo):

    next_empty = find_next_empty(bo)

    if (not next_empty):
        print(bo)
        return True
    else:
        row, col = next_empty

    # try all numbers
    for testVal in range(1, 10):
        if (is_valid(bo, testVal, row, col)):
            # update board with new valid value
            bo[row][col] = testVal

            # check if board is solved
            if (solve_board(bo)):
                return True

            bo[row][col] = x

    return False


def print_board(bo):
    for i in range(0, 9):
        row_string = ""
        if (i % 3 == 0):
            row_string += '  ' + '- ' * 12 + '\n'
        for j in range(0, 9):

            if (j % 3 == 0):
                row_string += ' | ' + str(bo[i][j])
            elif (j == 8):
                row_string += ' ' + str(bo[i][j]) + ' |'
            else:
                row_string += ' ' + str(bo[i][j])

        if (i == 8):
            row_string += '\n  ' + '- ' * 12
        print(row_string)


print('Sudoku...')
print_board(board)
solve_board(board)
