from settings.environment import default
import pygame

def load(path):
    return pygame.image.load(default.image_root + path)

icons = {
    "appicon": load("appicon.png")
}

backgrounds = {
    "main-screen": load("backgrounds/main_screen.png"),

    "França": load("backgrounds/countries/france.png"),
    "China": load("backgrounds/countries/china.png")
}

buttons = {
    "start_match": load("buttons/main_screen/start_match.png"),
    "choose_level": load("buttons/main_screen/choose_level.png"),
    "ranking": load("buttons/main_screen/ranking.png"),
    "how_play": load("buttons/main_screen/how_play.png"),
    "initial_active": load("buttons/main_screen/active.png"),

    "beginner": load("buttons/main_screen/beginner.png"),
    "normal": load("buttons/main_screen/normal.png"),
    "advanced": load("buttons/main_screen/advanced.png"),
    "professional": load("buttons/main_screen/professional.png"),
    "master": load("buttons/main_screen/master.png"),
}

modals = {
    "choose-levels": load("modals/choose_level.png"),
    "how_play": load("modals/how_play.png"),
    "ranking": load("modals/ranking.png")
}