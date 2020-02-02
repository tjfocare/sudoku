# Sudoku (Interactive Gui and CLI Solver)


Clone this repository
```bash
$ git clone https://github.com/tjfocare/sudoku
```

Install pipenv

```bash
$ pip3 install pipenv
$ cd <path_to_repository>/sudoku
$ pipenv shell
$ pipenv install
```

## Sudoku Solver using Backtracking (command-line)

To run sudoku solver

```bash
$ python3 run.py -solve -<no>
```

where *no* is between (0, 49). If *no* is omitted, a random number will be selected.

Ex.
```bash
$ python3 run.py -solve 0

puzzle no:  4

 | 0 0 3 | 0 2 0 | 6 0 0 |
 | 9 0 0 | 3 0 5 | 0 0 1 |
 | 0 0 1 | 8 0 6 | 4 0 0 |
  
 | 0 0 8 | 1 0 2 | 9 0 0 |
 | 7 0 1 | 0 0 0 | 0 0 8 |
 | 0 0 6 | 7 0 8 | 2 0 0 |

 | 0 0 2 | 6 0 9 | 5 0 0 |
 | 8 0 0 | 2 0 3 | 0 0 9 |
 | 0 0 5 | 0 1 0 | 3 0 0 |

Solved in 0:00:00.019869

  - - - - - - - - - - - - 
 | 5 2 3 | 8 1 6 | 7 4 9 |
 | 7 8 4 | 5 9 3 | 1 2 6 |
 | 6 9 1 | 4 7 2 | 8 3 5 |
  - - - - - - - - - - - - 
 | 2 3 9 | 1 4 5 | 6 8 7 |
 | 4 5 7 | 2 6 8 | 9 1 3 |
 | 1 6 8 | 9 3 7 | 2 5 4 |
  - - - - - - - - - - - - 
 | 3 4 2 | 7 8 9 | 5 6 1 |
 | 9 1 5 | 6 2 4 | 3 7 8 |
 | 8 7 6 | 3 5 1 | 4 9 2 |
  - - - - - - - - - - - - 
 ```

 ## Sudoku Gui (interactive)

 ```bash
 $ python3 run.py -gui
 ```
