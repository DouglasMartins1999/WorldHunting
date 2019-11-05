import pygame
from interfaces.BaseScreen import BaseScreen
from components.Fonts import text
from components.Color import level_colors
from components.Images import backgrounds, icons

class Dialog(BaseScreen):
    def __init__(self):
        super().__init__(backgrounds["dialogs"])
        self.phrases = [
            "Olá!! Meu nome é Josh! Acabei de chegar de várias viagens que fiz a todos os continentes! Conheci o Brasil, a França, a Austrália, a África, e até mesmo a China.",
            "Texto 2",
            "Texto 3",
        ]
        self.count = 0
        self.renderArrowDownButton()
        self.renderDialog()

    def renderDialog(self):
        posX = 50
        posY = 410

        phrase_wrapper = text(self.phrases[self.count], "asap/regular.ttf", 30, "#484848", (800, 140))
        self.mounted_screen = self.base_screen.copy()
        self.mounted_screen.blit(phrase_wrapper,  (posX, posY))

    def onClickNextPhrase(self, act):
        if self.count < len(self.phrases) - 1: 
            self.count += 1

    def renderArrowDownButton(self):
        self.addButton(icons["arrow_down"], (900, 460), (40, 36), self.onClickNextPhrase, self.base_screen)
        self.mounted_screen = self.base_screen.copy()
        
    def render(self):
        self.renderDialog()
        return self.mounted_screen