from settings.environment import default
import pygame

def load(path):
    return pygame.image.load(default.image_root + path)

icons = {
    "appicon": load("appicon.png"),

    "letter_box": load("buttons/match_screen/letter_box.png"),
    "cancel": load("buttons/match_screen/cancel.png"),
    "disable_sound": load("buttons/match_screen/disable_sound.png"),
    "enable_sound": load("buttons/match_screen/enable_sound.png"),
    "reveal_letter": load("buttons/match_screen/reveal_letter.png"),
    "hints_label": load("buttons/match_screen/hints.png"),
    "hint": {
        "prev": [
            load("buttons/match_screen/prev_hint_1.png"),
            load("buttons/match_screen/prev_hint_1.png"),
            load("buttons/match_screen/prev_hint_2.png"),
            load("buttons/match_screen/prev_hint_3.png"),
            load("buttons/match_screen/prev_hint_4.png"),
            load("buttons/match_screen/prev_hint_5.png")
        ],
        "next": [
            load("buttons/match_screen/next_hint_1.png"),
            load("buttons/match_screen/next_hint_1.png"),
            load("buttons/match_screen/next_hint_2.png"),
            load("buttons/match_screen/next_hint_3.png"),
            load("buttons/match_screen/next_hint_4.png"),
            load("buttons/match_screen/next_hint_5.png")
        ]
    }
}

backgrounds = {
    "main-screen": load("backgrounds/main_screen.png"),
    "blurred": load("backgrounds/blurred_bg.png"),

    "Brasil": load("backgrounds/countries/brazil.png"),
    "França": load("backgrounds/countries/france.png"),
    "China": load("backgrounds/countries/china.png"),
    "Austrália": load("backgrounds/countries/australia.png"),
    "África do Sul": load("backgrounds/countries/south_africa.png"),
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

badges = [
    load("badges/1_beginner.png"),
    load("badges/2_normal.png"),
    load("badges/3_advanced.png"),
    load("badges/4_profissional.png"),
    load("badges/5_master.png")
]

extras = {
    "winner": load("badges/winner.png"),
    "points": load("badges/points.png")
}