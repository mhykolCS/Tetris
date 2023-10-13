from settings import *
from class_objects import Button
from pgfunctions import *


def load_topscore_surface():

    return_image = pygame.image.load("assets/return_button.png").convert_alpha()
    return_button_clicked_down = False

    score_file = open("data/scores.txt", 'r')
    score_name = [" " for name in range(10)]
    score_number = [0 for number in range(10)]

    for i in range(10):
        score_name[i] = score_file.readline()
        score_name[i] = score_name[i].strip('\n')
        score_number[i] = score_file.readline()
        score_number[i] = score_number[i].strip('\n')

    score_curate = [" " for total in range(10)]

    for i in range(10):
        score_curate[i] = str(i+1) + ": " + score_name[i] + " || " + score_number[i]
        print(score_curate[i])

    score = [0 for x in range(10)]

    while True:
        clock.tick(FPS)
        pygame.display.update()


        score[0] = draw_text(score_curate[0], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 130)
        score[1] = draw_text(score_curate[1], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 150)
        score[2] = draw_text(score_curate[2], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 170)
        score[3] = draw_text(score_curate[3], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 190)
        score[4] = draw_text(score_curate[4], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 210)
        score[5] = draw_text(score_curate[5], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 230)
        score[6] = draw_text(score_curate[6], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 250)
        score[7] = draw_text(score_curate[7], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 270)
        score[8] = draw_text(score_curate[8], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 290)
        score[9] = draw_text(score_curate[9], SCORES_FONT, ROSE_Q, SURFACE_WIDTH / 2, 310)




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