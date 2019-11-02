import pygame
from components.Images import backgrounds, buttons, modals
from settings.environment import default
from interfaces.BaseScreen import BaseScreen
from services.Events import events, Action

class Initial(BaseScreen):
    def __init__(self):
        super().__init__(backgrounds["main-screen"])
        self.renderButtons()

    def renderButtons(self):
        self.addButton(buttons["start"], (73, 141), (205, 45), lambda act: print("OK"))
        self.addButton(buttons["start"], (73, 198), (205, 45), self.showRules)

    def showRules(self, act):
        rect = pygame.Rect(452, 24, 468, 478)
        self.mounted_screen.blit(modals["choose-levels"], rect)
        events.removeListener(act)

initial = Initial()