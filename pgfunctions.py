from settings import *


def draw_text(string, font, text_col, x, y):
    text = font.render(string, True, text_col)
    text_width = text.get_rect().width
    text_height = text.get_rect().height
    WINDOW.blit(text, (x - (text_width/2), y-(text_height/2)))
