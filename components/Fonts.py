import pygame
from settings.environment import default
from components.Color import toRGB
pygame.font.init()

def text(text = "", font_path = "asap/regular.ttf", size = 16, color = "#000000", dimensions = default.resolution):
    return pygame.font.Font(default.font_root + font_path, size).render(text, True, toRGB(color))