import pygame

import numpy as np

pygame.init()

win = pygame.display.set_mode((500, 500))

font_width = 50
font = pygame.font.SysFont('Comic Sans MS', font_width)

pygame.display.set_caption("Sudoku")

grid_size = 9
colour = (255, 255, 255)
x = 0

board = np.array([
    [1, 2, 3, x, x, x, x, x, x],
    [x, x, 4, x, x, x, x, x, x],
    [x, x, 3, x, x, x, x, x, x],
    [x, x, 2, x, x, x, x, 6, x],
    [x, x, 1, x, x, x, x, x, x],
    [x, x, x, x, x, 7, x, x, x],
    [x, x, x, x, x, x, x, x, x],
    [x, x, x, x, x, 1, x, x, x],
    [5, x, x, x, x, 8, 2, x, x],
])


def draw_grid():
    for i in range(1, grid_size):
        offset = i / grid_size
        # vertical
        start_pos = (win.get_width() * offset, 0)
        end_pos = (win.get_width() * offset, win.get_height())
        pygame.draw.line(win, colour, start_pos, end_pos)
        # horizontal
        start_pos = (0, win.get_height() * offset)
        end_pos = (win.get_width(), win.get_height() * offset)
        pygame.draw.line(win, colour, start_pos, end_pos)


def draw_sudoku(bo):
    for i in range(0, 9):
        for j in range(0, 9):
            number = font.render(str(bo[i][j]), True, colour)
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
                print('clicked in pos: ', i, j)
                return (i, j)


run = True


def handle_user_event(bo):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            run = False
        elif (event.type == pygame.MOUSEBUTTONUP):
            (row, col) = clicked_in_cell(pygame.mouse.get_pos())
            if (bo[row][col] == x):
                print('valid to click here')


while (run):
    pygame.time.delay(100)

    handle_user_event(board)

    draw_grid()
    draw_sudoku(board)

    pygame.display.update()

pygame.QUIT
