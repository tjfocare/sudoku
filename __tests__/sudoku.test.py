import unittest

import numpy as np

from board import Board, Cell

from sudoku import is_empty, is_in_col, is_in_row, is_in_square, is_valid_placement, print_board

x = 0

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


class TestIsEmpty(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_is_empty_top_left(self):
        self.assertTrue(is_empty(self.board, 0, 0))

    def test_is_empty_top_middle(self):
        self.assertTrue(is_empty(self.board, 0, 5))

    def test_is_empty_top_right(self):
        self.assertTrue(is_empty(self.board, 0, 8))

    def test_is_empty_boardttom_right(self):
        self.assertTrue(is_empty(self.board, 8, 8))


class TestGetValue(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_get_top(self):
        res = self.board.get_value(0, 2)
        self.assertEqual(res, 3)

    def test_get_top1(self):
        res = self.board.get_value(0, 0)
        self.assertEqual(res, x)

    def test_get_top2(self):
        res = self.board.get_value(0, 1)
        self.assertEqual(res, x)

    def test_get_top3(self):
        res = self.board.get_value(1, 0)
        self.assertEqual(res, 9)

    def test_get_top4(self):
        res = self.board.get_value(1, 1)
        self.assertEqual(res, x)

    def test_get_btm(self):
        res = self.board.get_value(6, 5)
        self.assertEqual(res, 9)


class TestIsInRow(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_is_not_in_row(self):
        self.assertFalse(is_in_row(self.board, 1, 0))

    def test_is_in_row(self):
        self.assertTrue(is_in_row(self.board, 3, 1))

    def test_is_in_row_btm(self):
        self.assertTrue(is_in_row(self.board, 5, 8))


class TestIsInCol(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_is_in_col(self):
        self.assertTrue(is_in_col(self.board, 9, 0))

    def test_is_in_col_btm(self):
        self.assertTrue(is_in_col(self.board, 7, 3))

    def test_is_not_in_col(self):
        self.assertFalse(is_in_col(self.board, 4, 3))


class TestIsInSquare(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_is_in_top_left(self):
        self.assertTrue(is_in_square(self.board, 3, 0, 0))

    def test_is_not_in_square_one(self):
        self.assertFalse(is_in_square(self.board, 8, 0, 0))

    def test_is_in_top_middle(self):
        self.assertTrue(is_in_square(self.board, 2, 1, 3))

    def test_is_in_top_right(self):
        self.assertTrue(is_in_square(self.board, 1, 1, 8))

    def test_is_in_mid_left(self):
        self.assertTrue(is_in_square(self.board, 8, 3, 2))

    def test_is_in_mid_mid(self):
        self.assertTrue(is_in_square(self.board, 8, 4, 4))

    def test_is_in_mid_right(self):
        self.assertTrue(is_in_square(self.board, 9, 4, 7))

    def test_is_in_bottom_left(self):
        self.assertTrue(is_in_square(self.board, 5, 7, 2))

    def test_is_in_bottom_mid(self):
        self.assertTrue(is_in_square(self.board, 9, 8, 4))

    def test_is_in_bottom_right(self):
        self.assertTrue(is_in_square(self.board, 3, 8, 8))


class TestIsValid(unittest.TestCase):

    def setUp(self):
        self.board = Board(grid)

    def test_is_valid_top_left(self):
        self.assertTrue(is_valid_placement(self.board, 5, 0, 0))

    def test_is_not_valid_top_left(self):
        self.assertFalse(is_valid_placement(self.board, 8, 0, 0))


if __name__ == '__main__':

    board = Board(grid)
    print_board(board)
    unittest.main()
