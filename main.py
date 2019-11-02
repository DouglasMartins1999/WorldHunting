from settings.environment import default
from components.Images import icons
import pygame, sys

pygame.init()
pygame.display.set_caption("World Hunting")
pygame.display.set_icon( icons["appicon"] )

main_screen = pygame.display.set_mode( (default.resX, default.resY) )

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    main_screen.fill((153, 153, 153))
    pygame.display.flip()