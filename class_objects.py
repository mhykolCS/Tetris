from settings import *


class Button:
    def __init__(self, xpos, ypos, scale, image):
        image_width = image.get_width()
        image_height = image.get_height()
        image = pygame.transform.smoothscale(image, (image_width * scale, image_height * scale))
        self.rect = image.get_rect()
        self.rect.topleft = (xpos - (image_width / 2 * scale), ypos - (image_height / 2 * scale))
        WINDOW.blit(image, (xpos - (image_width / 2 * scale), ypos - (image_height / 2 * scale)))

    def click_down(self):
        mouse_position = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_position):
            if pygame.mouse.get_pressed()[0]:
                return True

    def click_release(self):
        mouse_position = pygame.mouse.get_pos()
        if not pygame.mouse.get_pressed()[0]:
            return True

        if not self.rect.collidepoint(mouse_position):
            return False



