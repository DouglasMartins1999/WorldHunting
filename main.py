import pygame, sys
from components.Images import icons, buttons
from components.Fonts import text
from settings.environment import default
from services.Events import events

from interfaces.Initial import initial
from interfaces.Match import Match

from interfaces.Dialog import Dialog

from services.Session import GameSession

pygame.init()
pygame.display.set_caption("World Hunting")
pygame.display.set_icon( icons["appicon"] )

# Temporary Line
game = GameSession().getContries().addNewSession().game

main_screen = pygame.display.set_mode(default.resolution)
dialog = Dialog()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            events.callListeners(mouse)

    # main_screen.blit(Match(game.sessions[0]).render(), default.initial_pos)
    main_screen.blit(dialog.render(),  default.initial_pos)

    pygame.display.flip()