from settings import *
from pgfunctions import *
from class_objects import Button
from configure_surface import load_configure_surface
from topscore_surface import load_topscore_surface
from game_surface import load_game_surface


def load_startup_surface():

    # Images
    play_game_image = pygame.image.load("assets/play_game_button.png").convert_alpha()
    top_scores_image = pygame.image.load("assets/top_scores_button.png").convert_alpha()
    configure_image = pygame.image.load("assets/configure_button.png").convert_alpha()
    exit_game_image = pygame.image.load("assets/exit_game_button.png").convert_alpha()
    # end Images

    play_game_clicked_down = False
    top_scores_clicked_down = False
    configure_clicked_down = False
    exit_game_clicked_down = False

    while True:
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WINDOW.fill(BLACK)
        title_text = draw_text("TETRIS", TITLE_FONT, TITLE_FONT_COLOUR, SURFACE_WIDTH / 2, 80)

        play_game_button = Button(SURFACE_WIDTH / 2, 300, 1, play_game_image)
        top_scores_button = Button(SURFACE_WIDTH / 2, 450, 1, top_scores_image)
        configure_game_button = Button(SURFACE_WIDTH / 2, 550, 1, configure_image)
        exit_game_button = Button(SURFACE_WIDTH / 2, 650, 1, exit_game_image)

        if play_game_clicked_down:
            play_game_clicked_down = False
            if play_game_button.click_release():
                WINDOW.fill(BLACK)
                load_game_surface()
        if play_game_button.click_down() and not play_game_clicked_down:
            play_game_clicked_down = True

        if top_scores_clicked_down:
            top_scores_clicked_down = False
            if top_scores_button.click_release():
                WINDOW.fill(BLACK)
                load_topscore_surface()
        if top_scores_button.click_down() and not top_scores_clicked_down:
            top_scores_clicked_down = True

        if configure_clicked_down:
            configure_clicked_down = False
            if configure_game_button.click_release():
                WINDOW.fill(BLACK)
                load_configure_surface()
        if configure_game_button.click_down() and not configure_clicked_down:
            configure_clicked_down = True

        if exit_game_clicked_down:
            exit_game_clicked_down = False
            if exit_game_button.click_release():
                break
        if exit_game_button.click_down() and not exit_game_clicked_down:
            exit_game_clicked_down = True

    pygame.quit()
