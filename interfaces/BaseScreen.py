import pygame
from settings.environment import default
from services.Events import events, Action

class BaseScreen:
    def __init__(self, background = pygame.Surface(default.resolution)):
        self.base_screen = self.generateScreen(background)
        self.mounted_screen = self.base_screen.copy()
        events.clearListeners()

    def generateScreen(self, background):
        screen = pygame.Surface(default.resolution, pygame.SRCALPHA)
        screen.blit(background, default.initial_pos)
        return screen

    def addButton(self, surface, position = (0, 0), dimension = (0, 0), handler = None, dest = None):
        rect = pygame.Rect(position, dimension)
        action = Action(rect, handler)
        events.addListener(action)

        (dest or self.mounted_screen).blit(surface, rect)

    def render(self):
        return self.mounted_screen

class Window:
    def __init__(self, main = BaseScreen):
        self.current_screen = main().render
        self.stored_screens = {}

    def defineScreen(self, screen = BaseScreen, *args):
        self.current_screen = screen(*args).render
        return self

    def defineCreatedScreen(self, screen = BaseScreen()):
        self.current_screen = screen.render
        return self

    def storeScreen(self, title, screen):
        screen = StoredScreen(screen, events.actions)
        self.stored_screens[title] = screen
        return self

    def restorePrevScreen(self, title = None):
        try:
            s = self.stored_screens[title]
            self.current_screen = s.screen.render
            events.replaceAllListeners(s.listeners)
            return self
        except:
            return self

    def render(self):
        return self.current_screen()

class StoredScreen:
    def __init__(self, screen, listeners):
        self.screen = screen
        self.listeners = listeners

window = Window()