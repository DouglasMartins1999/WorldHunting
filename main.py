import pygame, sys
from components.Images import icons
from settings.environment import default

from interfaces.Initial import initial

pygame.init()
pygame.display.set_caption("World Hunting")
pygame.display.set_icon( icons["appicon"] )

main_screen = pygame.display.set_mode(default.resolution)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    main_screen.blit(initial.base_screen, default.initial_pos)
    pygame.display.flip()