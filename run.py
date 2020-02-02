import argparse
from src import board

parser = argparse.ArgumentParser(description='Sudoku Solver')
# parser.add_argument('--gui', nargs='?')
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-gui', action='store_true', default=False, help='Opens the Gui')
group.add_argument('-solve', action='store_true', default=False, help='Solves a selected sudoku (CLI)')

args = parser.parse_args()

if (args.gui):
    board.main()