import pygame
from settings.environment import default
from services.Events import events, Action

class BaseScreen:
    def __init__(self, background):
        self.base_screen = self.generateScreen(background)
        self.mounted_screen = self.base_screen.copy()
        events.clearListeners()

    def generateScreen(self, background):
        screen = pygame.Surface(default.resolution)
        screen.blit(background, default.initial_pos)
        return screen

    def addButton(self, surface, position = (0, 0), dimension = (0, 0), handler = None, dest = None):
        rect = pygame.Rect(position, dimension)
        action = Action(rect, handler)
        events.addListener(action)

        (dest or self.mounted_screen).blit(surface, rect)

    def render(self):
        return self.mounted_screen