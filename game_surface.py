from class_objects import Button
from pgfunctions import *
from random import choice


def load_game_surface():

    clock_count = 0
    dropping_clock_cycle = 60
    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False
    old_tetromino_tiles = None
    game_field = list(list(0 for h in range(GAME_H))for W in range(GAME_W))

    # GAME GRID
    game_grid = list(pygame.Rect(55 + x * TILE_SIZE, 100 + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                          for x in range(GAME_W)
                          for y in range(GAME_H))

    # Translates the tetromino_key into a tile position
    tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0)for x, y in tetromino_type)
                                    for tetromino_type in TETROMINO_KEY)
    current_tetromino_tile_pixels = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
    current_tetromino_tiles = choice(tetromino_tile_positions)

    while True:
        clock.tick(FPS)
        WINDOW.fill(BLACK)
        clock_count += 1
        list(pygame.draw.rect(WINDOW, ROSE_Q, individual_tile, 1) for individual_tile in game_grid)

        # Event Listening
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    move_approved = True
                    for i in range(4):
                        if current_tetromino_tiles[i].x < 1:
                            move_approved = False
                    if move_approved:
                        for i in range(4):
                            current_tetromino_tiles[i].x -= 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    move_approved = True
                    for i in range(4):
                        if current_tetromino_tiles[i].x > GAME_W - 2:
                            move_approved = False
                    if move_approved:
                        for i in range(4):
                            current_tetromino_tiles[i].x += 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    dropping_clock_cycle = 5
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    center = current_tetromino_tiles[0]
                    for i in range(4):
                        y = current_tetromino_tiles[i].x - center.x
                        x = current_tetromino_tiles[i].y - center.y
                        current_tetromino_tiles[i].x = center.x - x
                        current_tetromino_tiles[i].y = center.y + y
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    dropping_clock_cycle = 60

        # Downwards Movement
        if clock_count >= dropping_clock_cycle:
            move_approved = True
            for i in range(4):
                if current_tetromino_tiles[i].y > GAME_H - 2 or game_field[current_tetromino_tiles[i].x][current_tetromino_tiles[i].y+1] == 1:
                    move_approved = False
                    old_tetromino_tiles = current_tetromino_tiles
                    tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0)for x, y in tetromino_type)
                                    for tetromino_type in TETROMINO_KEY)
                    current_tetromino_tile_pixels = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
                    current_tetromino_tiles = choice(tetromino_tile_positions)
            if move_approved:
                for i in range(4):
                    current_tetromino_tiles[i].y += 1
            else:
                for i in range(4):
                    game_field[old_tetromino_tiles[i].x][old_tetromino_tiles[i].y] = 1
            clock_count = 0                   
                
        # Translates the tetromino_meta tile position into screen coordinates and draws
        for tile in range(4):
            current_tetromino_tile_pixels.x = 55 + 2 + current_tetromino_tiles[tile].x * TILE_SIZE
            current_tetromino_tile_pixels.y = 100 + 2 + current_tetromino_tiles[tile].y * TILE_SIZE
            pygame.draw.rect(WINDOW, GRAY, current_tetromino_tile_pixels)

        # Draw Game Field

        for i in range(GAME_W):
            for j in range(GAME_H):
                if game_field[i][j] == 1:
                    old = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
                    old.x = 55 + 2 + i * TILE_SIZE
                    old.y = 100 + 2 + j * TILE_SIZE
                    pygame.draw.rect(WINDOW, GRAY, old)

        # Clear Lines
            for row in range(GAME_H-1, 0, -1):
                count = 0
                for column in range(GAME_W-1):
                    if game_field[column][row]:
                        count += 1
                    else:
                        count = 0
                if count == 9:
                    for column_overwrite in range(GAME_W-1):
                        game_field[column_overwrite][row] = 0
                    for move_row in range(row, 0, -1):
                        for x in range(GAME_W-1):
                            game_field[column][move_row] = game_field[column][move_row-1] 

        # Return Button
        return_button = Button(SURFACE_WIDTH / 2 + SURFACE_WIDTH / 4, 750, 1, return_image)

        if return_button_clicked_down:
            return_button_clicked_down = False
            if return_button.click_release():
                WINDOW.fill(BLACK)
                return 0
        if return_button.click_down() and not return_button_clicked_down:
            return_button_clicked_down = True
            
        pygame.display.update()
