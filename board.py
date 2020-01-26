import enum

import pygame

import numpy as np

x = 0

font_width = 50

colour_danger = (255, 0, 0)
colour_info = (255, 255, 255)


# font = pygame.font.SysFont(None, font_width)


class TYPE(enum.Enum):
    ARRAY = 0
    GRID = 1


def print_cell(cell):
    row_string = 'touchable: ' + cell.touchable + ', '
    row_string += 'selected: ' + cell.is_selected + ', '
    row_string += 'value: ' + cell.value + ', '


class Board:
    def __init__(self, grid):
        self.grid = grid
        self.size = np.size(grid)
        self.selected_cell = ()

    def __eq__(self, other):
        if not isinstance(other, Board):
            return NotImplemented

        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != other.grid[i][j]:
                    return False

        return True

    def draw_cell(self, win, row, col, font):
        self.grid[row][col].draw(win, row, col, font)

    def get_grid(self, return_type=TYPE.GRID):
        if return_type == TYPE.GRID:
            return self.grid

        elif return_type == TYPE.ARRAY:
            grid = []
            for i in range(0, 9):
                row = []
                for j in range(0, 9):
                    row.append(self.get_value(i, j))
                grid.append(row)
            return grid

    def get_col(self, col):
        values = []
        for cell in self.grid[:, col]:
            values.append(cell.value)
        return values

    def get_row(self, row):
        values = []
        for cell in self.grid[row]:
            values.append(cell.value)
        return values

    def get_selected_cell(self):
        return self.selected_cell

    def get_value(self, row, col):
        return int(self.grid[row][col].value)

    def check_selected(self, row, col):
        return self.grid[row][col].is_selected

    def is_editable(self, row, col):
        return True if self.get_value(row, col) == x else False

    def check_finished(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j].value == x:
                    return False

        return True

    def set_cell(self, num, row, col):
        self.grid[row][col].value = int(num)
        self.grid[row][col].is_selected = False
        self.selected_cell = ()

    def set_grid(self, updated_grid):
        self.grid = updated_grid

    # assumes cell is touchable and can be cleared
    def clear_selected_cell(self):
        row, col = self.selected_cell
        self.grid[row][col] = Cell(x)
        self.selected_cell = ()

    def update_selected_cell(self, pos):
        for i in range(0, 9):
            for j in range(0, 9):
                self.grid[i][j].is_selected = False

        if pos is not None:
            row = pos[0]
            col = pos[1]
            self.grid[row][col].is_selected = True
            self.selected_cell = (row, col)
        else:
            self.clear_selected_cell()


# Cell class
class Cell:
    def __init__(self, value, is_selected=False):
        # user-editable cells - shouldn't change
        self.touchable = True if value == x else False
        self.is_selected = is_selected
        self.value = value

    def draw(self, win, row, col, font):
        text_colour = colour_danger if self.is_selected else colour_info
        number = font.render(str(self.value), True, text_colour)

        grid_width = win.get_width() / 9
        x_pos = grid_width / 2 + win.get_width() * col / 9 - font_width / 4
        y_pos = grid_width / 2 + win.get_height() * row / 9 - font_width / 4

        win.blit(number, (x_pos, y_pos))

        # draw red outline
        if self.is_selected:
            pygame.draw.rect(win, colour_danger,
                             (x_pos - font_width / 4, y_pos - font_width / 4, grid_width, grid_width), 3)
