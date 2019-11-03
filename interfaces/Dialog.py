import pygame
from interfaces.BaseScreen import BaseScreen
# from components.Fonts import text
from components.Images import backgrounds

class Dialog(BaseScreen):
    def __init__(self):
        # red = 212, 66, 66
        # size = width, height = 600, 400
        # screen = pygame.display.set_mode(size)
        # screen.fill(red)

        # self.mounted_screen = self.base_screen.copy()
        
        super().__init__(backgrounds["dialogs"])