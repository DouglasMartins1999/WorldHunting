from services.Crossword import Crossword
from settings.environment import default
from database.Words import countries
from datetime import datetime
from random import shuffle

class LevelSession:
    def __init__(self, game, level, countries):
        self.game = game
        self.level = level
        self.country = countries[level - 1]
        self.crossword = Crossword(self.country, self.level)
        self.start = None
        self.finish = None
        self.score = 0

    def startSession(self, date = None):
        self.start = date or datetime.now()
        return self

    def finishSession(self, date = None):
        self.finish = dae or datetime.now()
        return self

    def getScore(self):
        level = self.level
        time = self.finish.timestamp() - self.start.timestamp()
        self.score = round( ( level ** 2 * default.words_by_level ) / ( time / 500 ) ) * 100
        return self
        

class GameSession:
    def __init__(self):
        self.player = ""
        self.sessions = []
        self.countries = []
        self.level = 3

    def increaseLevel(self):
        self.level += 1
        return self

    def setPlayer(self, name = ""):
        self.player = name
        return self

    def getContries(self):
        self.countries = countries.copy()
        shuffle(self.countries)
        return self

    def addNewSession(self):
        self.increaseLevel()
        session = LevelSession(self, self.level, self.countries)
        self.sessions.append(session)
        return session

    def getGeralScore(self):
        score = 0
        for session in self.sessions:
            score += session.score
        return score