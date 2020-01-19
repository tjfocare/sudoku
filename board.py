import enum

import numpy as np

x = 0


class TYPE(enum.Enum):
    ARRAY = 0
    GRID = 1


class Board():
    def __init__(self, grid):
        self.grid = grid
        self.size = np.size(grid)
        self.selected_cell = ()

    def __eq__(self, other):
        if not isinstance(other, Board):
            return NotImplemented

        for i in range(0, 9):
            for j in range(0, 9):
                if (self.grid[i][j] != other.grid[i][j]):
                    return False

        return True

    def get_grid(self, return_type=TYPE.GRID):
        if (return_type == TYPE.GRID):
            return self.grid

        elif (return_type == TYPE.ARRAY):
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

    def set_grid(self, updated_grid):
        self.grid = updated_grid

    def update_selected_cell(self, except_pos):
        for i in range(0, 9):
            for j in range(0, 9):
                if (i == except_pos[0] and j == except_pos[1]):
                    self.grid[i][j].is_selected = True
                    self.selected_cell = (i, j)
                else:
                    self.grid[i][j].is_selected = False
        return self.grid


# Cell class
class Cell():
    def __init__(self, value, is_selected=False):
        self.empty = True if value == x else False
        self.is_selected = is_selected
        self.value = value
