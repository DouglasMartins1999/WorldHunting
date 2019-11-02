import pygame
from settings.environment import default
from components.Color import toRGB
pygame.font.init()


def text(text, font, size, color, dimensions, line_height = 1):
    font = pygame.font.Font(default.font_root + font, size)
    surface = pygame.Surface(dimensions, pygame.SRCALPHA)
    surface.fill((0, 0, 0, 0))
    
    rect = surface.get_rect()

    y = rect.top
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        if y + fontHeight > rect.bottom:
            break

        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        image = font.render(text[:i], True, toRGB(color))
        surface.blit(image, (rect.left, y))
        y += fontHeight + line_height
        text = text[i:]

    return surface