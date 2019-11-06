from services.Events import status
from services.Ranking import ranking
from interfaces.BaseScreen import BaseScreen, window
from components.Images import backgrounds, buttons, extras
from components.Fonts import text
from components.Song import mixer
from settings.environment import level_names

class EndMatch(BaseScreen):
    def __init__(self, session, MatchClass):
        super().__init__(backgrounds["blurred"])
        self.session = session
        self.match_screen = MatchClass
        self.basicElements()
        mixer.music.stop(400)
        mixer.addEffect("winner")

    def basicElements(self):
        time = self.session.getTime()
        start_btn = buttons["start_match"].copy()
        start_label = text("Próxima Fase", "asap/regular.ttf", 18, "#FFFFFF", (120, 25))
        start_btn.blit(start_label, (53, 12))

        basic_text = "Você conseguiu concluir o nível {} em {}:{} min. Sua pontuação nessa fase foi de {} pontos, e você tem {} pontos acumulados. Continue assim.".format(
            level_names[self.session.level],
            str(time[0]), str(time[1]),
            str(self.session.score),
            str(self.session.game.getGeralScore())
        )

        congrats = text("Parabéns!!", "righteous/regular.ttf", 56, "#373737", (284, 125))
        levels = text(str(self.session.level) + " de " + str(len(self.session.game.countries)) + " fases", "mclaren/regular.ttf", 14, "#777777", (90, 25))
        basic_text = text(basic_text, "asap/regular.ttf", 20, "#373737", (315, 140))

        score = extras["points"].copy()
        score_label = text(str(self.session.game.getGeralScore()), "asap/bold.ttf", 28, "#555555", (98, 35))
        score.blit(score_label, (45, 5))

        self.addButton(start_btn, (180, 395), (205, 45), self.startNextLevel, self.base_screen)
        self.base_screen.blit(congrats, (180, 120))
        self.base_screen.blit(levels, (180, 183))
        self.base_screen.blit(basic_text, (180, 237))
        self.base_screen.blit(extras["winner"], (562, 140))
        self.base_screen.blit(score, (640, 419))

        self.mounted_screen = self.base_screen.copy()

    def startNextLevel(self, act):
        mixer.addEffect("started")

        if self.session.game.checkNewSessionPossibility():
            self.session.game.addNewSession()
            window.defineScreen(self.match_screen, self.session.game.getCurrentLevel())
        else:
            game = self.session.game
            player = len(game.sessions)
            
            game.setPlayer("Player " + str(player))
            ranking.addPlayer(game.player, game.getGeralScore())
            ranking.sortRanking()
            window.restorePrevScreen("main_menu")