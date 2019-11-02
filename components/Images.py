from settings.environment import default
import pygame

icons = {
    "appicon": pygame.image.load(default.image_root + "appicon.png")
}

backgrounds = {
    "main-screen": pygame.image.load("{root}{folder}/main_screen.png".format(root = default.image_root, folder = "backgrounds"))
}