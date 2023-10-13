from class_objects import Button
from pgfunctions import *
from random import choice


def load_game_surface():

    clock_count = 0
    dropping_clock_cycle = 60
    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False
    continue_image = pygame.image.load("assets/continue_button.png").convert_alpha()
    continue_button_clicked_down = True
    old_tetromino_tiles = None
    game_field = list(list(0 for h in range(GAME_H))for W in range(GAME_W))
    score_int = 0
    lines_eliminated_int = 0
    current_level_int = 0
    escape_screen_active = 0
    
    

    # GAME GRID
    game_grid = list(pygame.Rect(55 + x * TILE_SIZE, 100 + y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                          for x in range(GAME_W)
                          for y in range(GAME_H))

    # Translates the tetromino_key into a tile position
    tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0)for x, y in tetromino_type)
                                    for tetromino_type in TETROMINO_KEY)
    current_tetromino_tile_pixels = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
    current_tetromino_tiles = choice(tetromino_tile_positions)
    

    tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0)for x, y in tetromino_type)
                                    for tetromino_type in TETROMINO_KEY)    
    next_tetromino = choice(tetromino_tile_positions)
    for tile in range(4):
        next_tetromino_tile_pixels = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
        next_tetromino_tile_pixels.x = 55 + 2 + next_tetromino[tile].x * TILE_SIZE
        next_tetromino_tile_pixels.y = 100 + 2 + next_tetromino[tile].y * TILE_SIZE
        pygame.draw.rect(WINDOW, GRAY, next_tetromino_tile_pixels)

    while True:
        clock.tick(FPS)
        clock_count += 1
        list(pygame.draw.rect(WINDOW, ROSE_Q, individual_tile, 1) for individual_tile in game_grid)

        # Text Rendering

        group_number = draw_text("Group Number: 33", REGULAR_FONT, ROSE_Q, 430, 110)
        
        score_str = "Score: {}".format(score_int)
        score = draw_text(score_str, REGULAR_FONT, ROSE_Q, 430, 130)
        
        lines_eliminated_str = "Lines: {}".format(lines_eliminated_int)
        lines_eliminated = draw_text(lines_eliminated_str, REGULAR_FONT, ROSE_Q, 430, 150)
        
        current_level_str = "Level: {}".format(current_level_int)
        current_level = draw_text(current_level_str, REGULAR_FONT, ROSE_Q, 430, 170)

        game_mode = draw_text("Game: Normal", REGULAR_FONT, ROSE_Q, 430, 190)
        
        play_mode = draw_text("Mode: Player", REGULAR_FONT, ROSE_Q, 430, 210)


        next_block_text = draw_text("Next Block", REGULAR_FONT, ROSE_Q, 430, 250)
        
        
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
                elif event.key == pygame.K_ESCAPE:
                    escape_screen_active = 1
                    
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
                    current_tetromino_tiles = next_tetromino
                    tetromino_tile_positions = list(list(pygame.Rect(x + GAME_W / 2, y + 1, 0, 0)for x, y in tetromino_type)
                                    for tetromino_type in TETROMINO_KEY)
                    next_tetromino = choice(tetromino_tile_positions)
                    next_tetromino_tile_pixels = pygame.Rect(0, 0, TILE_SIZE - 4, TILE_SIZE - 4)
                    next_tetromino_tile_pixels.x = 430 + next_tetromino[tile].x * TILE_SIZE
                    next_tetromino_tile_pixels.y = 280 + next_tetromino[tile].y * TILE_SIZE
                    pygame.draw.rect(WINDOW, GRAY, next_tetromino_tile_pixels)
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
            for column in range(GAME_W):
                if game_field[column][row]:
                    count += 1
                else:
                    count = 0

            if count == 10:
                for row_overwrite in range(row, 0, -1):
                    for column_overwrite in range(GAME_W):
                        game_field[column_overwrite][row_overwrite] = 0
                        game_field[column_overwrite][row_overwrite] = game_field[column_overwrite][row_overwrite-1]
                        

        if escape_screen_active:
            clock_count = 0
            escape_rect = pygame.Rect(SURFACE_WIDTH / 2 - 100, SURFACE_HEIGHT / 2 - 100, 200, 200)
            pygame.draw.rect(WINDOW, JET, escape_rect)
            return_button = Button(SURFACE_WIDTH / 2, SURFACE_HEIGHT / 2 - 60, 1, return_image)
            continue_button = Button(SURFACE_WIDTH /2, SURFACE_HEIGHT / 2 + 60, 1, continue_image)

            if return_button_clicked_down:
                return_button_clicked_down = False
                if return_button.click_release():
                    WINDOW.fill(BLACK)
                    
                    return 0
            if return_button.click_down() and not return_button_clicked_down:
                return_button_clicked_down = True
                
            if continue_button_clicked_down:
                continue_button_clicked_down = False
                if continue_button.click_release():
                    WINDOW.fill(BLACK)
                    escape_screen_active = 0
            if continue_button.click_down() and not continue_button_clicked_down:
                continue_button_clicked_down = True
        
            
        pygame.display.update()
        WINDOW.fill(BLACK)
