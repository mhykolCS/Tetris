from settings import *
from class_objects import Button
from pgfunctions import *


def load_configure_surface():
    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False
    
    two_image = pygame.image.load("assets/two.png").convert_alpha()
    four_image = pygame.image.load("assets/four.png").convert_alpha()
    six_image = pygame.image.load("assets/six.png").convert_alpha()
    eight_image = pygame.image.load("assets/eight.png").convert_alpha()
    twelve_image = pygame.image.load("assets/twelve.png").convert_alpha()
    normal_image = pygame.image.load("assets/normal.png").convert_alpha()
    extended_image = pygame.image.load("assets/extended.png").convert_alpha()
    player_image = pygame.image.load("assets/player.png").convert_alpha()
    ai_image = pygame.image.load("assets/ai.png").convert_alpha()

    while True:
        clock.tick(FPS)
        pygame.display.update()

        two_button = Button(SURFACE_WIDTH / 2, 150, 0.6, two_image)
        four_button_field = Button(SURFACE_WIDTH / 2, 100, 0.6, four_image)
        four_button_level = Button(SURFACE_WIDTH / 2 +  50, 150, 0.6, four_image)
        six_button = Button(SURFACE_WIDTH / 2 + 100, 150, 0.6, six_image)
        eight_button = Button(SURFACE_WIDTH / 2 + 50, 100, 0.6, eight_image)
        twelve_button = Button(SURFACE_WIDTH / 2 + 100, 100, 0.6, twelve_image)
        normal_button = Button(SURFACE_WIDTH / 2 + 20, 200, 0.6, normal_image)
        extended_button = Button(SURFACE_WIDTH / 2 + 150, 200, 0.6, extended_image)
        player_button = Button(SURFACE_WIDTH / 2 + 20, 250, 0.6, player_image)
        ai_button = Button(SURFACE_WIDTH / 2 + 150, 250, 0.6, ai_image)


        field_size_text = draw_text("Field Size: ", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 4, 100)
        game_level_text = draw_text("Game Level: ", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 4, 150)
        game_type_text = draw_text("Game Type: ", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 4, 200)
        game_mode_text = draw_text("Game Mode: ", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 4, 250)


        return_button = Button(SURFACE_WIDTH / 2, 600, 1, return_image)

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