import unittest

from sudoku import is_empty, is_valid, is_in_col, is_in_square, is_in_row

import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)


x = 'X'
board = [
        [x, x, x, 2, x, x, x, 9, 6],
        [x, 3, 2, 7, x, 9, x, 4, 8],
        [x, x, x, x, 1, 2, x, 2, x],
        [x, 4, x, x, 8, 1, 2, x, x],
        [x, x, 8, x, 3, x, 9, x, x],
        [x, x, 5, 9, 7, x, x, 6, x],
        [x, 9, x, 1, 6, x, x, x, x],
        [8, 2, x, 5, x, 9, 7, 1, x],
        [4, 7, x, x, x, 8, x, x, x],
]


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

    def test_is_in_row(board, self):
        self.assertTrue(is_in_row(board, 3, 1))


class TestIsInCol(unittest.TestCase):

    def test_is_in_col(self):
        self.assertTrue(is_in_col(board, 8, 0))

    def test_is_not_in_col(self):
        self.assertFalse(is_in_col(board, 4, 3))


if __name__ == '__main__':
    unittest.main()
