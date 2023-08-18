from settings import *
from class_objects import Button
from pgfunctions import *


def load_topscore_surface():

    clock = pygame.time.Clock()
    return_image = pygame.image.load("assets/return_button.png").convert_alpha()

    while True:
        clock.tick(FPS)
        pygame.display.update()

        return_button = Button(SURFACE_WIDTH / 2, 600, 1, return_image)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 1

        if return_button.click_event():
            return 0
