from database.Words import countries
from services.LevelSession import LevelSession
from random import shuffle

class GameSession:
    def __init__(self):
        self.player = player
        self.sessions = []
        self.contries = []
        self.level = 0

    def increaseLevel(self):
        self.level += 1
        return self

    def setPlayer(self, name = ""):
        self.player = name
        return self

    def getContries(self):
        self.contries = countries.copy()
        shuffle(self.contries)
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