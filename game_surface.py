import pygame

from settings import *
from class_objects import Button
from pgfunctions import *


def load_game_surface():

    clock_count = 0
    dropping_clock_cycle = 60

    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False

    # GAME GRID
    tile_locations = list(pygame.Rect(55 + x * TILE_SIZE, 100 + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                          for x in range(GAME_W)
                          for y in range(GAME_H))

    # Translates the tetromino_key into a tile position
    tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0)for x, y in tetromino_type)
                                    for tetromino_type in TETROMINO_KEY)
    tetromino_rect = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
    tetromino_meta = tetromino_tile_positions[6]

    while True:
        clock.tick(FPS)
        clock_count += 1
        pygame.display.update()
        WINDOW.fill(BLACK)
        tile_rect = list(pygame.draw.rect(WINDOW, ROSE_Q, individual_tile, 1) for individual_tile in tile_locations)

        # Event Listening
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    move_approved = True
                    for i in range(4):
                        if tetromino_meta[i].x < 1:
                            move_approved = False
                    if move_approved:
                        for i in range(4):
                            tetromino_meta[i].x -= 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    move_approved = True
                    for i in range(4):
                        if tetromino_meta[i].x > GAME_W - 2:
                            move_approved = False
                    if move_approved:
                        for i in range(4):
                            tetromino_meta[i].x += 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    dropping_clock_cycle = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    dropping_clock_cycle = 60

        # Downwards Movement
        if clock_count >= dropping_clock_cycle:
            move_approved = True
            for i in range(4):
                if tetromino_meta[i].y > GAME_H - 2:
                    move_approved = False
            if move_approved:
                for i in range(4):
                    tetromino_meta[i].y += 1
            clock_count = 0


        # Translates the tetromino_meta tile position into screen coordinates and draws
        for tile in range(4):
            tetromino_rect.x = 55 + 2 + tetromino_meta[tile].x * TILE_SIZE
            tetromino_rect.y = 100 + 2 + tetromino_meta[tile].y * TILE_SIZE
            pygame.draw.rect(WINDOW, GRAY, tetromino_rect)

        # Return Button
        return_button = Button(SURFACE_WIDTH / 2 + SURFACE_WIDTH / 4, 750, 1, return_image)

        if return_button_clicked_down:
            return_button_clicked_down = False
            if return_button.click_release():
                WINDOW.fill(BLACK)
                return 0
        if return_button.click_down() and not return_button_clicked_down:
            return_button_clicked_down = True
