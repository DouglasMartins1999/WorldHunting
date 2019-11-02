from interfaces.BaseScreen import BaseScreen
from components.Images import backgrounds
from components.Fonts import text
from components.Color import level_colors
from services.LevelSession import LevelSession

class Match(BaseScreen):
    def __init__(self, level_session = LevelSession(None, 1, [])):
        super().__init__(backgrounds[level_session.coutry["name"]])
        self.session = level_session
        self.color = level_colors[self.session.level]
        self.staticElements()

    def staticElements(self):
        level = text("Nível {}".format(self.session.level), "asap/bold.ttf", 16, self.color, (60, 18))
        self.base_screen.blit(level, (74, 45))
