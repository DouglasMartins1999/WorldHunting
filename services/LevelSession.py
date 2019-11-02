from services.Crossword import Crossword
from settings.environment import default
from datetime import datetime

class LevelSession:
    def __init__(self, game, level, countries):
        self.game = game
        self.level = level
        self.coutry = countries[level - 1]
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
    