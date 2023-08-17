from settings import *
from pgfunctions import *
from configure_surface import load_configure_surface
from topscore_surface import load_topscore_surface
from game_surface import load_game_surface


def load_startup_surface():
    # Active Surfaces
    startup_surface_active = True
    configure_surface_active = False
    topscore_surface_active = False
    game_surface_active = False
    # end Active Surfaces

    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if startup_surface_active:
            WINDOW.fill(BLACK)
            draw_text("TETRIS", TITLEFONT, TITLEFONTCOLOUR, SURFACE_WIDTH / 2, 80)

        if configure_surface_active:
            load_configure_surface()
            configure_surface_active = False
            startup_surface_active = True

        if topscore_surface_active:
            load_topscore_surface()
            topscore_surface_active = False
            startup_surface_active = True

        if game_surface_active:
            load_game_surface()
            game_surface_active = False
            startup_surface_active = True

    pygame.quit()
