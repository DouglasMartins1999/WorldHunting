class Default:
    def __init__(self):
        self.resolution = (1024, 576)
        self.initial_pos = (0, 0)
        self.words_by_level = 3
        self.image_root = "assets/images/"
        self.font_root = "assets/fonts/"
        self.song_root = "assets/songs/"

default = Default()

level_names = [
    "Default",
    "Iniciante",
    "Normal",
    "Avançado",
    "Profissional",
    "Master"
]