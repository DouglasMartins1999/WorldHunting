import pygame
from interfaces.BaseScreen import BaseScreen, window
from components.Fonts import text
from components.Color import level_colors
from components.Images import backgrounds, icons

class Dialog(BaseScreen):
    def __init__(self, screen = None, *args):
        super().__init__(backgrounds["dialogs"])
        self.phrases = [
            "Olá!! Meu nome é Josh! Acabei de chegar de várias viagens que fiz a todos os continentes! Conheci o Brasil, a França, a Austrália, a África, e até mesmo a China.",
            "Trouxe na minha mala experiências, lembranças e conhecimentos que gostaria que fossem compartilhadas com você,",
            "Por isso, hoje a sua missão é viajar para Países pelos quais passei e aprender um pouco mais sobre eles. :)",
        ]
        self.count = 0
        self.renderArrowDownButton()
        self.renderDialog()
        self.screen_args = args
        self.next_screen = screen

    def renderDialog(self):
        posX = 50
        posY = 410

        phrase_wrapper = text(self.phrases[self.count], "asap/regular.ttf", 30, "#484848", (800, 140))
        self.mounted_screen = self.base_screen.copy()
        self.mounted_screen.blit(phrase_wrapper,  (posX, posY))

    def onClickNextPhrase(self, act):
        if self.count < len(self.phrases) - 1: 
            self.count += 1
        elif self.next_screen != None:
            window.defineScreen(self.next_screen, *self.screen_args)

    def renderArrowDownButton(self):
        self.addButton(icons["arrow_down"], (900, 460), (40, 36), self.onClickNextPhrase, self.base_screen)
        self.mounted_screen = self.base_screen.copy()
        
    def render(self):
        self.renderDialog()
        return self.mounted_screen