import pygame
from components.Images import backgrounds
from settings.environment import default

class Initial:
    def __init__(self):
        self.base_screen = self.generateScreen()

    def generateScreen(self):
        screen = pygame.Surface(default.resolution)
        screen.blit(backgrounds["main-screen"], default.initial_pos)
        return screen

initial = Initial()