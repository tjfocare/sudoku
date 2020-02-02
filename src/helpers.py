import csv, re

import numpy as np

from board import Cell

def read_boards():
    boards = np.array([[]])
    board_lines = open('sudoku.txt', 'r').readlines()

    for line in board_lines:
        if not re.match('[A-Za-z]+\s[0-9]*', line):
            if re.match('[\n]', line[-1]):
                grid_row = list(line)[:-1]
            else:
                grid_row = list(line)
            boards = np.append(boards, grid_row)

    return np.reshape(boards, (-1, 9))

def get_grid(boards, no):
    integer_board = np.array(boards[no * 9: no * 9 + 9, :], int)

    grid = []
    for i in range(0, 9):
        row = []
        for j in range(0, 9):
            value = integer_board[i][j]
            row.append(Cell(value))
        grid.append(row)
    grid = np.array(grid)

    return grid

def print_board(bo):
    for i in range(0, 9):
        row_string = ""
        if i % 3 == 0:
            row_string += '  ' + '- ' * 12 + '\n'
        for j in range(0, 9):

            if j % 3 == 0:
                row_string += ' | ' + str(bo.get_value(i, j))
            elif j == 8:
                row_string += ' ' + str(bo.get_value(i, j)) + ' |'
            else:
                row_string += ' ' + str(bo.get_value(i, j))

        if i == 8:
            row_string += '\n  ' + '- ' * 12
        print(row_string)
