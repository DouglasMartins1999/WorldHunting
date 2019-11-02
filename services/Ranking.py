class Player:
    def __init__(self, player, score):
        self.player = player
        self.score = score

class Ranking:
    def __init__(self):
        self.players = []

        self.players.append(Player("Robert", 6843))
        self.players.append(Player("Lilian", 6192))
        self.players.append(Player("Jackson", 5210))
        self.players.append(Player("Diana", 4036))
        self.players.append(Player("Pietro", 3745))

        self.sortRanking()

    def addPlayer(self, player, score):
        player = Player(player, score)
        self.players.append(player)
        self.sortRanking()
        return self

    def sortRanking(self):
        self.players.sort(key = lambda player: player.score, reverse = True)
        return self
        
ranking = Ranking()