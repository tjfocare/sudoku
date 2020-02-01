import path, csv, re, random, sys, warnings

from datetime import datetime

import numpy as np

from board import Board, Cell, TYPE

from pathlib import Path, PureWindowsPath

x = 0

boards = np.array([[]])

data_folder = path.Path("__tests__")
test_file = data_folder / "sudoku.txt"
test = open(test_file, 'r').readlines()
test = open('__tests__/sudoku.txt', 'r').readlines()

# filename = Path("__tests__/sudoku.txt")

# Convert path to Windows format
# test_file = PureWindowsPath(filename)
# test = open(test_file, 'r').readlines()

# print(path_on_windows)

for line in test:
    if not re.match('[A-Za-z]+\s[0-9]*', line):
        if re.match('[\n]', line[-1]):
            grid_row = list(line)[:-1]
        else:
            grid_row = list(line)
        boards = np.append(boards, grid_row)

boards = np.reshape(boards, (-1, 9))

# max 50
# if len(sys.argv) > 1:
#     board_no = int(sys.argv[1])
# else:
#     board_no = random.randint(0, 49)

# print('puzzle no: ', board_no)

# grid = np.array([
#     [Cell(x), Cell(x), Cell(3), Cell(x), Cell(
#         2), Cell(x), Cell(6), Cell(x), Cell(x)],
#     [Cell(9), Cell(x), Cell(x), Cell(3), Cell(
#         x), Cell(5), Cell(x), Cell(x), Cell(1)],
#     [Cell(x), Cell(x), Cell(1), Cell(8), Cell(
#         x), Cell(6), Cell(4), Cell(x), Cell(x)],
#     [Cell(x), Cell(x), Cell(8), Cell(1), Cell(
#         x), Cell(2), Cell(9), Cell(x), Cell(x)],
#     [Cell(7), Cell(x), Cell(x), Cell(x), Cell(
#         x), Cell(x), Cell(x), Cell(x), Cell(8)],
#     [Cell(x), Cell(x), Cell(6), Cell(7), Cell(
#         x), Cell(8), Cell(2), Cell(x), Cell(x)],
#     [Cell(x), Cell(x), Cell(2), Cell(6), Cell(
#         x), Cell(9), Cell(5), Cell(x), Cell(x)],
#     [Cell(8), Cell(x), Cell(x), Cell(2), Cell(
#         x), Cell(3), Cell(x), Cell(x), Cell(9)],
#     [Cell(x), Cell(x), Cell(5), Cell(x), Cell(
#         1), Cell(x), Cell(3), Cell(x), Cell(x)],
# ])


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


steps = 0

def solve_board(bo):
    global steps_taken
    next_empty = find_next_empty(bo)

    if not next_empty:
        print('winner')
        print_board(bo)
        return True
    else:
        row, col = next_empty

    # try all numbers
    for testVal in range(1, 10):
        steps_taken = steps_taken + 1
        if is_valid_placement(bo, testVal, row, col):
            # update board with new valid value
            bo.set_cell(testVal, row, col)

            # check if board is solved
            if solve_board(bo):
                return True

            bo.set_cell(x, row, col)

    return False


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

def main():
    global steps
    board = Board(grid)

    start_time = datetime.now()

    print('Sudoku...')
    print_board(board)
    print('solving...')
    solve_board(board)

    end_time = datetime.now()
    time_diff = (end_time - start_time) #.strftime('%H:%M:%S')
    print('Solved in ' + str(time_diff) + ' with '  + str(steps) + ' steps.')

def write_results():
    global steps_taken

    with open('test_results.csv', mode='w') as csv_file:
        csv_writer = csv.writer(
            csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(['Puzzle no.', 'Time to complete', 'No. of steps'])

        for no in range(0, 4):
            board_no = no
            # 0:9, 9:18, 18:27, 27:36
            integer_board = np.array(boards[board_no * 9: board_no * 9 + 9, :], int)

            # setup grid
            grid = []
            for i in range(0, 9):
                row = []
                for j in range(0, 9):
                    value = integer_board[i][j]
                    row.append(Cell(value))
                grid.append(row)
            grid = np.array(grid)

            steps_taken = 0
            board = Board(grid)

            start_time = datetime.now()
            print_board(board)
            print('solving... puzzle: ', board_no)
            solve_board(board)

            end_time = datetime.now()
            time_diff = (end_time - start_time) #.strftime('%H:%M:%S')

            csv_writer.writerow([board_no, str(time_diff), steps_taken])


# main()
# write_results()
