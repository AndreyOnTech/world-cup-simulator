class Team:

    def __init__(self, dados, team, groupID) -> None:
        self.points = 0
        self.gm = 0
        self.gs = 0
        self.name = team
        self.groupID = groupID

        self.pointsFifa = dados[team]['Points']
        self.rank = dados[team]['Rank']
        pass

    @property
    def saldo(self):
        return self.gm - self.gs
    
    def clear(self):
        self.points = 0
        self.gm = 0
        self.gs = 0

