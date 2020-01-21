import re

import random

import sys

import warnings

import numpy as np

from board import Board, Cell, TYPE

# warnings.simplefilter(action='ignore', category=FutureWarning)

x = 0

boards = np.array([[]])

test = open('./sudoku.txt', 'r').readlines()

for line in test:
    if (not re.match('[A-Za-z]+\s[0-9]*', line)):
        if (re.match('[\n]', line[-1])):
            grid_row = list(line)[:-1]
        else:
            grid_row = list(line)
        boards = np.append(boards, grid_row)

boards = np.reshape(boards, (-1, 9))

# max 50
if (len(sys.argv) > 1):
    board_no = int(sys.argv[1])
else:
    board_no = random.randint(0, 49)

# print('puzzle no: ', board_no)

# 0:9, 9:18, 18:27, 27:36
# board = np.array(boards[board_no * 9: board_no * 9 + 9, :], int)

def is_empty(bo, row, col):
    return bo.get_value(row, col) == x


def is_in_row(bo, num, row):
    return int(num) in bo.get_row(row)


def is_in_col(bo, num, col):
    return int(num) in bo.get_col(col)


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

    square = np.array(np.multiply(bo.get_grid(TYPE.ARRAY), window), int)

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
        print_board(bo)
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
                row_string += ' | ' + str(bo.get_value(i, j))
            elif (j == 8):
                row_string += ' ' + str(bo.get_value(i, j)) + ' |'
            else:
                row_string += ' ' + str(bo.get_value(i, j))

        if (i == 8):
            row_string += '\n  ' + '- ' * 12
        print(row_string)


# print('Sudoku...')
# print_board(board)
# solve_board(board)
