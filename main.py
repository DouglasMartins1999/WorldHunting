import pygame, sys
from components.Images import icons, buttons
from components.Fonts import text
from settings.environment import default
from services.Events import events

from interfaces.Initial import initial

pygame.init()
pygame.display.set_caption("World Hunting")
pygame.display.set_icon( icons["appicon"] )

main_screen = pygame.display.set_mode(default.resolution)
texta = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam rutrum risus enim, nec hendrerit justo sagittis vitae. Vivamus nec ornare tellus. Vestibulum in porta ante, ut convallis mi."

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            events.callListeners(mouse)

    main_screen.blit(initial.render(), default.initial_pos)
    main_screen.blit(text(texta, "asap/bold.ttf", 32, "#FFFFFF"), (200, 300))
    pygame.display.flip()