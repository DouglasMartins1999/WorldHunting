from settings.environment import default
import pygame

def load(path):
    return pygame.image.load(default.image_root + path)

icons = {
    "appicon": load("appicon.png")
}

backgrounds = {
    "main-screen": load("backgrounds/main_screen.png")
}

buttons = {
    "start": load("buttons/start.png")
}

modals = {
    "choose-levels": load("modals/choose_level.png")
}