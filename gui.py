import pygame

import re

import numpy as np

from sudoku import is_valid

# TODO:
# - update Sudoku to support Cell
# - refactor cell and board to Board class

# Initialise window
pygame.init()
pygame.display.set_caption("Sudoku")
win = pygame.display.set_mode((500, 500))

# Initialise font variables
font_width = 50
font = pygame.font.SysFont('Comic Sans MS', font_width)

# Board class


class Board():
    def __init__(self, bo):
        self.bo = bo
        self.size = np.size(bo)
        self.selected_cell = ()

    def get_board(self):
        return self.bo

    def get_col(self, col):
        values = np.array([])
        for cell in self.bo[:, col]:
            np.append(values, cell.value)
        return values

    def get_row(self, row):
        values = np.array([])
        for cell in self.bo[row]:
            np.append(values, cell.value)
        return values

    def get_selected_cell(self):
        return self.selected_cell

    def get_value(self, row, col):
        return self.bo[row][col]

    def check_selected(self, row, col):
        return self.bo[row][col].is_selected

    def set_board(self, updated_board):
        self.bo = updated_board


# Cell class
class cell():
    def __init__(self, value, is_selected=False):
        self.empty = True if value == x else False
        self.is_selected = is_selected
        self.value = value


""" Constants: TODO extract to file """

# Sudoku grid size 9x9
grid_size = 9
# Text
colour = (255, 255, 255)
# Selected cell
colour_active = (255, 0, 0)
# Empty cell - TODO: refactor Board class
x = 0
# Num

""" End of Constants"""


""" Globals """

grid = np.array([
    [cell(1), cell(2), cell(3), cell(x), cell(
        x), cell(x), cell(x), cell(x), cell(x)],
    [cell(x), cell(x), cell(4), cell(x), cell(
        x), cell(x), cell(x), cell(x), cell(x)],
    [cell(x), cell(x), cell(3), cell(x), cell(
        x), cell(x), cell(x), cell(x), cell(x)],
    [cell(x), cell(x), cell(2), cell(x), cell(
        x), cell(x), cell(x), cell(6), cell(x)],
    [cell(x), cell(x), cell(1), cell(x), cell(
        x), cell(x), cell(x), cell(x), cell(x)],
    [cell(x), cell(x), cell(x), cell(x), cell(
        x), cell(7), cell(x), cell(x), cell(x)],
    [cell(x), cell(x), cell(x), cell(x), cell(
        x), cell(x), cell(x), cell(x), cell(x)],
    [cell(x), cell(x), cell(x), cell(x), cell(
        x), cell(1), cell(x), cell(x), cell(x)],
    [cell(5), cell(x), cell(x), cell(x), cell(
        x), cell(8), cell(2), cell(x), cell(x)],
])

board = Board(grid)

run = True

selected_cell = ()

""" End of Globals """

# def reset_board(bo):


def update_selected_cell(bo, except_pos):
    global selected_cell
    for i in range(0, 9):
        for j in range(0, 9):
            if (i == except_pos[0] and j == except_pos[1]):
                bo[i][j].is_selected = True
                selected_cell = (i, j)
            else:
                bo[i][j].is_selected = False
    return bo


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
            print(bo.get_value(i, j))
            # Set cell colour
            if (bo.check_selected(i, j)):
                number = font.render(
                    str(bo.get_value(i, j)), True, colour_active)
            else:
                number = font.render(str(bo.get_value(i, j)), True, colour)

            # print(number)
            grid_width = win.get_width() / 9
            x_pos = grid_width / 2 + win.get_width() * i / 9 - font_width / 4
            y_pos = grid_width / 2 + win.get_height() * j / 9 - font_width / 4
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
                return (i, j)


def handle_user_event(bo):
    global run
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
        elif (event.type == pygame.MOUSEBUTTONUP):
            (row, col) = clicked_in_cell(pygame.mouse.get_pos())
            if (bo.get_value(row, col) == x):
                bo.set_board(update_selected_cell(bo.get_board(), (row, col)))
        elif (event.type == pygame.KEYDOWN):
            print(selected_cell)
            if (re.match('\d', selected_key := chr(event.key)) and selected_cell):
                print('number input: ', selected_key)
                # print('valid number: ', is_valid(
                #     bo, selected_key, selected_cell[0], selected_cell[1]))


while (run):
    handle_user_event(board)

    draw_grid()
    draw_sudoku(board)

    pygame.display.update()

pygame.QUIT
