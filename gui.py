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
# Num

""" End of Constants"""


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
        # vertical gridline
        start_pos = (win.get_width() * offset, 0)
        end_pos = (win.get_width() * offset, win.get_height())
        pygame.draw.line(win, colour, start_pos, end_pos)
        # horizontal gridline
        start_pos = (0, win.get_height() * offset)
        end_pos = (win.get_width(), win.get_height() * offset)
        pygame.draw.line(win, colour, start_pos, end_pos)


def draw_sudoku(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            # Set Cell colour
            if (bo.check_selected(i, j)):
                number = font.render(
                    str(bo.get_value(i, j)), True, colour_active)
            else:
                number = font.render(str(bo.get_value(i, j)), True, colour)

            # print('val: ', i, j, str(bo.get_value(i, j)))
            grid_width = win.get_width() / 9
            x_pos = grid_width / 2 + win.get_width() * j / 9 - font_width / 4
            y_pos = grid_width / 2 + win.get_height() * i / 9 - font_width / 4
            win.blit(number, (x_pos, y_pos))


def clicked_in_Cell(click_pos):
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
                return (i, j)


def handle_user_event(bo):
    global run
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
        elif (event.type == pygame.MOUSEBUTTONUP):
            (row, col) = clicked_in_Cell(pygame.mouse.get_pos())
            if (bo.get_value(row, col) == x):
                updated_grid = bo.update_selected_cell((row, col))
                bo.set_grid(updated_grid)
        elif (event.type == pygame.KEYDOWN):
            selected_key = chr(event.key)
            if (re.match('\\d', selected_key) and bo.get_selected_cell):
                (selected_row, selected_col) = bo.get_selected_cell()
                print('valid number: ', is_valid(
                    bo, selected_key, selected_row, selected_col))


while (run):
    handle_user_event(board)

    draw_grid()
    draw_sudoku(board)

    pygame.display.update()

pygame.QUIT
