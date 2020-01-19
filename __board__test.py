from board import Board, Cell

# from gui import update_selected_cell

import unittest

import numpy as np

x = 0

grid = np.array([
    [Cell(1), Cell(2), Cell(3), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(4), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(3), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(2), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(6), Cell(x)],
    [Cell(x), Cell(x), Cell(1), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(x), Cell(x), Cell(
        x), Cell(7), Cell(x), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(x), Cell(x), Cell(
        x), Cell(x), Cell(x), Cell(x), Cell(x)],
    [Cell(x), Cell(x), Cell(x), Cell(x), Cell(
        x), Cell(1), Cell(x), Cell(x), Cell(x)],
    [Cell(5), Cell(x), Cell(x), Cell(x), Cell(
        x), Cell(8), Cell(2), Cell(x), Cell(x)],
])


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_get_value(self):
        res = self.board.get_value(0, 2)
        self.assertEqual(res, 3)

    def test_get_grid(self):
        new_board = Board(grid)
        self.assertTrue(new_board == self.board)

    def test_get_col(self):
        actual = [1, x, x, x, x, x, x, x, 5]
        res = self.board.get_col(0)
        self.assertEqual(res, actual)

    def test_get_row(self):
        actual = [1, 2, 3, x, x, x, x, x, x]
        res = self.board.get_row(0)
        self.assertEqual(res, actual)


class TestGuiLogic(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_update_selected(self):
        updated_grid = self.board.update_selected_cell((1, 1))
        updated_board = Board(updated_grid)
        self.assertTrue(updated_board.check_selected(1, 1))


if __name__ == '__main__':
    unittest.main()
