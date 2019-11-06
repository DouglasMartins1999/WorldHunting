import pygame
from components.Images import backgrounds, buttons, modals
from components.Fonts import text
from components.Song import mixer
from settings.environment import default
from interfaces.BaseScreen import BaseScreen, window
from interfaces.StartMatch import StartMatch
from interfaces.Match import Match
from services.Events import events, status, Action
from services.Ranking import ranking

class Initial(BaseScreen):
    def __init__(self):
        super().__init__(backgrounds["main-screen"])
        self.renderButtons()
        mixer.addBackground("menu", True)

    def renderButtons(self):
        start = buttons["start_match"].copy()
        level = buttons["choose_level"].copy()
        ranking = buttons["ranking"].copy()
        rules = buttons["how_play"].copy()

        start.blit(text("Iniciar Partida", "asap/regular.ttf", 18, "#FFFFFF", (120, 25)), (53, 12))
        level.blit(text("Escolher Level", "asap/regular.ttf", 18, "#FFFFFF", (120, 25)), (53, 12))
        ranking.blit(text("Meu Ranking", "asap/regular.ttf", 18, "#FFFFFF", (120, 25)), (53, 12))
        rules.blit(text("Como Jogar?", "asap/regular.ttf", 18, "#FFFFFF", (120, 25)), (53, 12))

        self.addButton(start, (73, 141), (205, 45), self.startMatch, self.base_screen)
        self.addButton(level, (73, 198), (205, 45), self.showLevels, self.base_screen)
        self.addButton(ranking, (73, 255), (205, 45), self.showRanking, self.base_screen)
        self.addButton(rules, (73, 312), (205, 45), self.showRules, self.base_screen)

        self.mounted_screen = self.base_screen.copy()

    def showLevels(self, act):
        rect = pygame.Rect(452, 24, 468, 478)
        self.mounted_screen = self.base_screen.copy()
        self.mounted_screen.blit(modals["choose-levels"], rect)

        self.addButton(buttons["beginner"], (532, 146), (185, 102), None)
        self.addButton(buttons["normal"], (729, 146), (185, 102), None)
        self.addButton(buttons["advanced"], (532, 260), (185, 102), None)
        self.addButton(buttons["professional"], (729, 260), (185, 102), None)
        self.addButton(buttons["master"], (532, 365), (185, 102), None)

    def showRules(self, act):
        rect = pygame.Rect(452, 24, 468, 478)
        rules = """Acompanhe Josh e o retorno de suas aventuras internacionais através de cruzadinhas que o farão aprender bastante.
                                                                                                                                                                                                
        O jogo é constituido de 5 fases, uma de cada país que Josh visitou. Seu objetivo é terminar as cruzadinhas no menor tempo possível, consultando as dicas que nosso instrutor disponibiliza. Quando descobrir uma palavra, não esqueça de consultar mais detalhes para enriquecer seu vocabulário e continuar aprendendo.                                                                                                                    
        Clique em uma linha ou coluna para começar a digitar. As palavras corretas serão identificadas automaticamente. Você pode pedir dicas clicando em \"?\", se quiser cancelar, basta tocar no botão power, divirta-se!"""

        self.mounted_screen = self.base_screen.copy()
        self.mounted_screen.blit(modals["how_play"], rect)
        self.mounted_screen.blit(text(rules, "mclaren/regular.ttf", 13, "#4D4D4D", (370, 352)), (532, 141))

    def showRanking(self, act):
        rect = pygame.Rect(452, 24, 468, 478)
        pos_name = (530, 140)
        pos_score = (815, 135)
        colors = ["#3ABA5E", "#3AB2BA", "#4E85DD", "#9D5EC3", "#F47588"]

        self.mounted_screen = self.base_screen.copy()
        self.mounted_screen.blit(modals["ranking"], rect)

        for index, p in enumerate(ranking.players):
            name = text(p.player, "asap/medium.ttf", 28, colors[index], (220, 35))
            score = text(str(p.score), "mclaren/regular.ttf", 32, "#4D4D4D", (85, 50))

            self.mounted_screen.blit(name, pos_name)
            self.mounted_screen.blit(score, pos_score)

            pos_name = (pos_name[0], pos_name[1] + 77)
            pos_score = (pos_score[0], pos_score[1] + 77)

    def startMatch(self, act):
        mixer.addEffect("started")
        status.createGame()
        status.getLastGame().addNewSession().startSession()
        window.defineScreen(StartMatch, status.getLastGame().sessions[0])

initial = Initial()