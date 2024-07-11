import pygame
import sys
import time
import random


pygame.init()


WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)


FONT = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

player = 1

start_time = time.time()

def draw_lines():
    screen.fill(BG_COLOR)
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = 'X' if player == 1 else 'O'

def available_square(row, col):
    return board[row][col] is None

def board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def check_win(player):
    symbol = 'X' if player == 1 else 'O'
    for row in range(BOARD_ROWS):
        if all([cell == symbol for cell in board[row]]):
            return True
    for col in range(BOARD_COLS):
        if all([board[row][col] == symbol for row in range(BOARD_ROWS)]):
            return True
    if all([board[i][i] == symbol for i in range(BOARD_ROWS)]) or all([board[i][BOARD_ROWS - i - 1] == symbol for i in range(BOARD_ROWS)]):
        return True
    return False


def computer_move():
    available_moves = [(row, col) for row in range(BOARD_ROWS) for col in range(BOARD_COLS) if available_square(row, col)]
    move = random.choice(available_moves)
    mark_square(move[0], move[1], 2)


def main():
    global player
    draw_lines()
    running = True
    game_over = False
    mode = 'player_vs_computer'  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    draw_figures()
                    end_time = time.time()
                    game_time = end_time - start_time
                    print(f"Time of game: {game_time:.2f} seconds")

                    if check_win(player):
                        game_over = True

                    player = 2 if player == 1 else 1

        if mode == 'player_vs_computer' and player == 2 and not game_over:
            computer_move()
            draw_figures()
            end_time = time.time()
            game_time = end_time - start_time
            print(f"Time of game: {game_time:.2f} seconds")

            if check_win(2):
                game_over = True

            player = 1

        pygame.display.update()

if __name__ == '__main__':
    main()
