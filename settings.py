import pygame

pygame.init()
clock = pygame.time.Clock()

# Colours
GRAY = (172, 189, 186)
AZURE = (205, 221, 221)
ROSE_Q = (165, 153, 181)
JET = (46, 47, 47)
BLACK = (5, 16, 20)

# Window Specifics
SURFACE_WIDTH = 500
SURFACE_HEIGHT = 800
WINDOW = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
pygame.display.set_caption("Tetris!! - Group 33")

# Game Specifics
FPS = 60
TITLE_FONT = pygame.font.SysFont("showcardgothic", 80)
REGULAR_FONT = pygame.font.SysFont("impact", 18)
SCORES_FONT = pygame.font.SysFont("impactlight", 30)
TITLE_FONT_COLOUR = ROSE_Q

GAME_W = 10
GAME_H = 20
TILE_SIZE = 30

TETROMINO_KEY = [
    [[0, 0], [0, 1], [-1, 1], [-1, 0]],     # Square Tetromino
    [[0, 0], [-1, 0], [0, 1], [0, 2]],      # "J" Tetromino
    [[0, 0], [1, 0], [0, 1], [0, 2]],       # "L" Tetromino
    [[0, 0], [-1, 0], [0, 1], [1, 1]],     # "S" Tetromino
    [[0, 0], [1, 0], [0, 1], [-1, 1]],     # "Z" Tetromino
    [[0, 0], [0, -1], [0, 1], [0, 2]],      # Line Tetromino
    [[0, 0], [-1, 1], [0, 1], [1, 1]]       # "T" Tetromino
]






