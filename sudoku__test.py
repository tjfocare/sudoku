import unittest

import numpy as np

from sudoku import is_empty, is_in_col, is_in_row, is_in_square, is_valid


x = 0
board = np.array([
    [x, x, x, 2, x, x, x, 9, 6],
    [x, 3, 2, 7, x, 9, x, 4, 8],
    [x, x, x, x, 1, 2, x, 2, x],
    [x, 4, x, x, 8, 1, 2, x, x],
    [x, x, 8, x, 3, x, 9, x, x],
    [x, x, 5, 9, 7, x, x, 6, x],
    [x, 9, x, 1, 6, x, x, x, x],
    [8, 2, x, 5, x, 9, 7, 1, x],
    [4, 7, x, x, x, 8, x, x, x],
])


class TestIsEmpty(unittest.TestCase):

    def test_is_empty_top_left(self):
        self.assertTrue(is_empty(board, 0, 0))

    def test_is_empty_top_middle(self):
        self.assertTrue(is_empty(board, 0, 5))

    def test_is_empty_top_right(self):
        self.assertFalse(is_empty(board, 0, 8))

    def test_is_empty_boardttom_right(self):
        self.assertTrue(is_empty(board, 8, 8))


class TestIsInRow(unittest.TestCase):

    def test_is_not_in_row(self):
        self.assertFalse(is_in_row(board, 1, 0))

    def test_is_in_row(self):
        self.assertTrue(is_in_row(board, 3, 1))


class TestIsInCol(unittest.TestCase):

    def test_is_in_col(self):
        self.assertTrue(is_in_col(board, 8, 0))

    def test_is_not_in_col(self):
        self.assertFalse(is_in_col(board, 4, 3))


class TestIsInSquare(unittest.TestCase):

    def test_is_in_top_left(self):
        self.assertTrue(is_in_square(board, 3, 0, 0))

    def test_is_not_in_square_one(self):
        self.assertFalse(is_in_square(board, 9, 0, 0))

    def test_is_in_top_middle(self):
        self.assertTrue(is_in_square(board, 4, 3, 1))

    def test_is_in_top_right(self):
        self.assertTrue(is_in_square(board, 8, 3, 2))

    def test_is_in_mid_left(self):
        self.assertTrue(is_in_square(board, 7, 1, 3))

    def test_is_in_mid_mid(self):
        self.assertTrue(is_in_square(board, 8, 4, 4))

    def test_is_in_mid_right(self):
        self.assertTrue(is_in_square(board, 1, 7, 5))

    def test_is_in_boardttom_left(self):
        self.assertTrue(is_in_square(board, 9, 2, 6))

    def test_is_in_boardttom_mid(self):
        self.assertTrue(is_in_square(board, 6, 5, 7))

    def test_is_in_boardttom_right(self):
        self.assertTrue(is_in_square(board, 1, 8, 8))


class TestIsValid(unittest.TestCase):

    def test_is_valid_top_left(self):
        self.assertTrue(is_valid(board, 1, 0, 0))

    def test_is_not_valid_top_left(self):
        self.assertFalse(is_valid(board, 8, 0, 0))


if __name__ == '__main__':
    unittest.main()
