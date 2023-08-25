from settings import *
from class_objects import Button
from pgfunctions import *


def load_topscore_surface():

    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False
    score = [0 for x in range(10)]

    while True:
        clock.tick(FPS)
        pygame.display.update()


        score[0] = draw_text("1: Person1 || 1,421,100", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 130)
        score[1] = draw_text("2: Person2 || 1,210,800", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 150)
        score[2] = draw_text("3: Person3 || 1,005,200", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 170)
        score[3] = draw_text("4: Person4 || 873,000", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 190)
        score[4] = draw_text("5: Person5 || 855,100", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 210)
        score[5] = draw_text("6: Person6 || 724,800", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 230)
        score[6] = draw_text("7: Person7 || 700,500", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 250)
        score[7] = draw_text("8: Person8 || 558,300", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 270)
        score[8] = draw_text("9: Person9 || 550,900", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 290)
        score[9] = draw_text("10: Person10 || 378,400", SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 310)




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