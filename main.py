import pygame, sys
from components.Images import icons
from settings.environment import default
from services.Events import events, keyboard

from interfaces.Initial import initial
from interfaces.Match import Match

from interfaces.Dialog import Dialog

from services.Session import GameSession
from interfaces.BaseScreen import window
from interfaces.Initial import Initial

pygame.init()
pygame.display.set_caption("World Hunting")
pygame.display.set_icon( icons["appicon"] )

main_screen = pygame.display.set_mode(default.resolution)
main_screen.fill((255, 255, 255))
window.defineScreen(Initial)

dialog = Dialog()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            events.callListeners(event.pos)
        if event.type == pygame.KEYDOWN:
            keyboard.printLetters(event.key)

    main_screen.blit(dialog.render(),  default.initial_pos)
    pygame.display.flip()