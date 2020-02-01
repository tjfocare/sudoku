import pygame

import re

import numpy as np

from sudoku import is_valid_placement

from board import Board, Cell

# Initialise window
pygame.init()
pygame.display.set_caption('Sudoku')
win = pygame.display.set_mode((500, 500))

# Initialise font variables
font_width = 50
font = pygame.font.SysFont(None, font_width)

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
        if i % 3 == 0:
            row_string += '  ' + '- ' * 12 + '\n'
        for j in range(0, 9):

            if j % 3 == 0:
                row_string += ' | ' + str(bo.check_selected(i, j))
            elif j == 8:
                row_string += ' ' + str(bo.check_selected(i, j)) + ' |'
            else:
                row_string += ' ' + str(bo.check_selected(i, j))

        if i == 8:
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
    [Cell(7), Cell(x), Cell(x), Cell(x), Cell(
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


def draw_board(bo):
    win.fill((0, 0, 0))

    draw_grid()

    for i in range(0, 9):
        for j in range(0, 9):
            # refactor all draw functionality to single draw fn in board
            bo.draw_cell(win, i, j, font)


def clicked_in_cell(click_pos):
    for i in range(0, 9):
        for j in range(0, 9):
            grid_left_edge = win.get_width() * i / 9
            grid_top_edge = win.get_height() * j / 9

            grid_right_edge = win.get_width() * (i + 1) / 9
            grid_btm_edge = win.get_height() * (j + 1) / 9

            if (grid_left_edge <= click_pos[0] < grid_right_edge and
                    grid_top_edge <= click_pos[1] < grid_btm_edge):
                return j, i


def handle_user_event(bo):
    global run
    updated_board = bo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # click in cell
        elif event.type == pygame.MOUSEBUTTONUP:
            (row, col) = clicked_in_cell(pygame.mouse.get_pos())

            if bo.is_editable(row, col):
                updated_board.update_selected_cell((row, col))
                # print_board(updated_board)

        # keypress events
        elif event.type == pygame.KEYDOWN:
            selected_key = chr(event.key)

            # input number
            if re.match('\\d', selected_key) and bo.get_selected_cell():
                (selected_row, selected_col) = bo.get_selected_cell()

                if is_valid_placement(bo, selected_key, selected_row, selected_col):
                    updated_board.set_cell(selected_key, selected_row, selected_col)

            # clear cell
            elif selected_key == pygame.K_ESCAPE:
                if bo.is_editable(row, col):
                    updated_board.update_selected_cell(None)

    return updated_board


def main():
    board = Board(grid)
    clock = pygame.time.Clock()

    while run:
        board = handle_user_event(board)
        # print_board(board)

        draw_board(board)

        if board.check_finished():
            print('winner')

        pygame.display.update()
        pygame.display.flip()
        clock.tick(60)


# if __name__ == 'main':
main()

pygame.quit()
