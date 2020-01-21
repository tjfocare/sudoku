import pygame

import re

import numpy as np

from sudoku import is_valid

from board import Board, Cell

# Initialise window
pygame.init()
pygame.display.set_caption("Sudoku")
win = pygame.display.set_mode((500, 500))

# Initialise font variables
font_width = 50
font = pygame.font.SysFont('Comic Sans MS', font_width)


""" Constants: TODO extract to file """

# Sudoku grid size 9x9
grid_size = 9
# Text
colour = (255, 255, 255)
# Selected Cell
colour_active = (255, 0, 0)
# Empty Cell - TODO: refactor Board class
x = 0
grid_has_changed = False

""" End of Constants"""


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


""" Globals """

grid = np.array([
    [Cell(x), Cell(x), Cell(3), Cell(x), Cell(
        2), Cell(x), Cell(6), Cell(x), Cell(x)],
    [Cell(9), Cell(x), Cell(x), Cell(3), Cell(
        x), Cell(5), Cell(x), Cell(x), Cell(1)],
    [Cell(x), Cell(x), Cell(1), Cell(8), Cell(
        x), Cell(6), Cell(4), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(8), Cell(1), Cell(
        x), Cell(2), Cell(9), Cell(x), Cell(x)],
    [Cell(7), Cell(x), Cell(1), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(x), Cell(8)],
    [Cell(x), Cell(x), Cell(6), Cell(7), Cell(
        x), Cell(8), Cell(2), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(2), Cell(6), Cell(
        x), Cell(9), Cell(5), Cell(x), Cell(x)],
    [Cell(8), Cell(x), Cell(x), Cell(2), Cell(
        x), Cell(3), Cell(x), Cell(x), Cell(9)],
    [Cell(x), Cell(x), Cell(5), Cell(x), Cell(
        1), Cell(x), Cell(3), Cell(x), Cell(x)],
])

board = Board(grid)

run = True

""" End of Globals """


def draw_grid():
    for i in range(1, grid_size):
        offset = i / grid_size
        thickness = 5 if i % 3 == 0 else 1

        # vertical gridline
        start_pos = (win.get_width() * offset, 0)
        end_pos = (win.get_width() * offset, win.get_height())
        pygame.draw.line(win, colour, start_pos, end_pos, thickness)

        # horizontal gridline
        start_pos = (0, win.get_height() * offset)
        end_pos = (win.get_width(), win.get_height() * offset)
        pygame.draw.line(win, colour, start_pos, end_pos, thickness)


def draw_sudoku(bo):
    global grid_has_changed
    for i in range(0, 9):
        for j in range(0, 9):

            # Set Cell colour
            if (grid_has_changed):
                number = font.render(
                    str(bo.get_value(i, j)), True, (0, 0, 0))
                grid_has_changed = False
            elif (bo.check_selected(i, j)):
                number = font.render(
                    str(bo.get_value(i, j)), True, colour_active)
            else:
                number = font.render(str(bo.get_value(i, j)), True, colour)

            grid_width = win.get_width() / 9
            x_pos = grid_width / 2 + win.get_width() * j / 9 - font_width / 4
            y_pos = grid_width / 2 + win.get_height() * i / 9 - font_width / 4
            win.blit(number, (x_pos, y_pos))


def clicked_in_cell(click_pos):
    for i in range(0, 9):
        for j in range(0, 9):
            grid_left_edge = win.get_width() * i / 9
            grid_top_edge = win.get_height() * j / 9

            grid_right_edge = win.get_width() * (i + 1) / 9
            grid_btm_edge = win.get_height() * (j + 1) / 9

            if (click_pos[0] >= grid_left_edge and
                click_pos[0] < grid_right_edge and
                click_pos[1] >= grid_top_edge and
                    click_pos[1] < grid_btm_edge):
                return (j, i)


def handle_user_event(bo):
    global run, grid_has_changed
    updatedBoard = bo

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False

        # click in cell
        elif (event.type == pygame.MOUSEBUTTONUP):
            (row, col) = clicked_in_cell(pygame.mouse.get_pos())

            if (bo.get_value(row, col) == x):
                updated_grid = bo.update_selected_cell((row, col))
                updatedBoard.set_grid(updated_grid)

        # keypress events
        elif (event.type == pygame.KEYDOWN):
            selected_key = chr(event.key)

            # digit keypress
            if (re.match('\\d', selected_key) and bo.get_selected_cell):
                (selected_row, selected_col) = bo.get_selected_cell()
                valid_input = is_valid(
                    bo, selected_key, selected_row, selected_col)

                if (valid_input):
                    updatedBoard.set_cell(
                        selected_key, selected_row, selected_col)
                    grid_has_changed = True

    return updatedBoard


while (run):
    pygame.display.flip()

    board = handle_user_event(board)
    print_board(board)

    draw_grid()
    draw_sudoku(board)

    pygame.display.update()

pygame.QUIT
