import pygame
import sys
import numpy as np

pygame.init()

(width, height) = (600, 600)
line_width = 12
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 45
# the value is for color rgb: red green blue
Red = (255, 0, 0)
background_color = (50, 140, 180)
line_color = (90, 50, 30)
circle_color = (250, 230, 210)
cross_color = (100, 100, 100)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Python TIC TAC TOE")
screen.fill(background_color)

board = np.zeros((board_rows, board_cols))

def draw_lines():
    # for horizontal line
    pygame.draw.line(screen, line_color, (0, 200), (600, 200), line_width)
    pygame.draw.line(screen, line_color, (0, 400), (600, 400), line_width)

    # vertical line
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), line_width)
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), line_width)

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, circle_color, (int(col * 200 + 100), int(row*200 + 100)), circle_radius, circle_width )
            elif board[row][col] == 2:
                pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + 200 - space), (col * 200 + 200 - space, row * 200 + space), cross_width)
                pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + space), (col * 200 + 200 - space, row * 200 + 200 - space), cross_width)

def mark_box(row, col, player):
    board[row][col] = player

def available_box(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def full_board():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def win_condition(player):
    # rules for vertical win
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # rules for horizontal win
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # rules for ascending diagonal win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # rules for descending diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), 15)

def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), 15)

def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = cross_color
    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 15)

def restart():
    screen.fill(background_color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_box(clicked_row, clicked_col):
                if player == 1:
                    mark_box(clicked_row, clicked_col, 1)
                    if win_condition(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_box(clicked_row, clicked_col, 2)
                    if win_condition(player):
                        game_over = True
                    player = 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()