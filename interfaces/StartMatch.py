from interfaces.BaseScreen import BaseScreen, window
from interfaces.Match import Match
from interfaces.Dialog import Dialog
from components.Images import backgrounds, badges, buttons
from components.Fonts import text
from components.Song import mixer

class StartMatch(BaseScreen):
    def __init__(self, session):
        super().__init__(backgrounds["blurred"])
        self.session = session
        self.basicElements()

    def basicElements(self):
        words_amount = len(self.session.crossword.structure)
        start_btn = buttons["start_match"].copy()
        start_label = text("Iniciar Partida", "asap/regular.ttf", 18, "#FFFFFF", (120, 25))
        start_btn.blit(start_label, (53, 12))

        country_label = text("País: " + self.session.country["name"], "asap/semibold.ttf", 27, "#373737", (220, 35))
        words_label = text(str(words_amount) + " palavras ocultas", "asap/italic.ttf", 20, "#5E5D5D", (220, 35))

        self.base_screen.blit(badges[self.session.level - 1], (295, 55))
        self.base_screen.blit(country_label, (247, 448))
        self.base_screen.blit(words_label, (247, 478))

        self.addButton(start_btn, (586, 452), (205, 45), self.startMatch, self.base_screen)
        self.mounted_screen = self.base_screen.copy()
        
    def startMatch(self, act):
        mixer.addEffect("started")

        if self.session.level == 1:
            window.defineScreen(Dialog, Match, self.session, StartMatch)
        else:
            window.defineScreen(Match, self.session, StartMatch)