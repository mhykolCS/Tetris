from settings import *


def draw_text(string, font, text_col, xpos, ypos):
    text = font.render(string, True, text_col)
    text_width = text.get_rect().width
    text_height = text.get_rect().height
    WINDOW.blit(text, (xpos - (text_width/2), ypos-(text_height/2)))
    return text

