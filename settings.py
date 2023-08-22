import pygame

pygame.init()
clock = pygame.time.Clock()

# Colours
GRAY = (172, 189, 186)
AZURE = (205, 221, 221)
ROSEQ = (165, 153, 181)
JET = (46, 47, 47)
BLACK = (5, 16, 20)

# Window Specifics
SURFACE_WIDTH = 500
SURFACE_HEIGHT = 800
WINDOW = pygame.display.set_mode((SURFACE_WIDTH, SURFACE_HEIGHT))
pygame.display.set_caption("Tetris!! - Group 33")

# Game Specifics
FPS = 60
TITLEFONT = pygame.font.SysFont("showcardgothic", 80)
TITLEFONTCOLOUR = ROSEQ

GAME_FIELD = None
GAME_FIELD.OUTER_X = 5
GAME_FIELD.OUTER_Y = 5
GAME_FIELD.OUTER_HEIGHT = 100
GAME_FIELD.OUTER_WIDTH = 50
GAME_FIELD.INNER_X = 10
GAME_FIELD.INNER_Y = 10
GAME_FIELD.INNER_HEIGHT = 90
GAME_FIELD.INNER_WIDTH = 90





