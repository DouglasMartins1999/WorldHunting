import pygame, sys
from components.Images import icons, buttons
from components.Fonts import text
from settings.environment import default
from services.Events import events, keyboard

from interfaces.Initial import Initial
from interfaces.Match import Match

from interfaces.BaseScreen import Window

from services.Session import GameSession

pygame.init()
pygame.display.set_caption("World Hunting")
pygame.display.set_icon( icons["appicon"] )

# Temporary Line
game = GameSession().getContries().addNewSession().game

main_screen = pygame.display.set_mode(default.resolution)
match = Match(game.sessions[0])
window = Window(Initial)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            events.callListeners(event.pos)
        if event.type == pygame.KEYDOWN:
            window.defineScreen(Match, game.sessions[0])
            keyboard.printLetters(event.key)

    main_screen.blit(window.render(), default.initial_pos)
    pygame.display.flip()