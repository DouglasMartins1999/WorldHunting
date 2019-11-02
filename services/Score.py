from datetime import datetime

class Score:
    def getScore(self, level = 1, words = 5, start_time = datetime.now(), finish_time = datetime.now()):
        time = finish_time.timestamp() - start_time.timestamp()
        return round( ( words * level ) / ( time / 500 ) ) * 100

    def sumScore(self, *scores):
        score = 0
        for s in scores:
            score += s
        return score