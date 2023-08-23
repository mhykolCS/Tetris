from settings import *
from class_objects import Button
from pgfunctions import *


def load_game_surface():

    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False

    while True:
        clock.tick(FPS)
        pygame.display.update()

        # GAME GRID
        tile_locations = list(pygame.Rect(55 + x * TILE_SIZE, 100 + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                     for x in range(GAME_W)
                     for y in range(GAME_H))
        tile_rect = list(pygame.draw.rect(WINDOW, ROSE_Q, individual_tile, 1) for individual_tile in tile_locations)

        # Translates the tetromino_key into a tile position
        tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0) for x, y in tetromino_type)
                          for tetromino_type in TETROMINO_KEY)
        tetromino_rect = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
        tetromino = tetromino_tile_positions[2]

        # Translates the tetromino tile position into screen coordinates
        for tile in range(4):
            tetromino_rect.x = 55 + 2 + tetromino[tile].x * TILE_SIZE
            tetromino_rect.y = 100 + 2 + tetromino[tile].y * TILE_SIZE
            pygame.draw.rect(WINDOW, GRAY, tetromino_rect)

        # Return Button
        return_button = Button(SURFACE_WIDTH / 2 + SURFACE_WIDTH / 4, 750, 1, return_image)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 1

        if return_button_clicked_down:
            return_button_clicked_down = False
            if return_button.click_release():
                WINDOW.fill(BLACK)
                return 0
        if return_button.click_down() and not return_button_clicked_down:
            return_button_clicked_down = True
