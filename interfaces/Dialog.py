import pygame
from interfaces.BaseScreen import BaseScreen
from components.Fonts import text
from components.Color import level_colors
from components.Images import backgrounds

class Dialog(BaseScreen):
    def __init__(self):
        super().__init__(backgrounds["dialogs"])
        phrase = "Olá!! Meu nome é Josh! Acabei de chegar de várias viagens que fiz a todos os continentes! Conheci o Brasil, a França, a Austrália, a África, e até mesmo a China."

        phrase_wrapper = text(phrase, "asap/regular.ttf", 30, "#484848", (800, 140))
        posX = 50
        posY = 410
        self.mounted_screen.blit(phrase_wrapper,  (posX, posY))