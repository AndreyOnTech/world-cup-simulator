from Team import Team
from Match import play_match

import math

class Group:

    def __init__(self, dados, groupID:str, team1:str, team2:str, team3:str, team4:str):
        self.dados = dados
        self.groupID = groupID
        self.team1 = Team(dados, team1, groupID)
        self.team2 = Team(dados, team2, groupID)
        self.team3 = Team(dados, team3, groupID)
        self.team4 = Team(dados, team4, groupID)

        self.matches = []
        

    def match(self, team1, team2):
        resultado, gols1, gols2 = play_match(team1, team2)

        self.matches.append(f'{team1.name} {gols1} X {gols2} {team2.name}')

        team1.gm += gols1
        team1.gs += gols2

        team2.gm += gols2
        team2.gs += gols1

        if resultado == "TIME1":
            team1.points += 3

        elif resultado == "TIME2":
            team2.points += 3

        else:
            team1.points += 1
            team2.points += 1


    def group_exec(self):
        self.team1.clear()
        self.team2.clear()
        self.team3.clear()
        self.team4.clear()
        self.matches.clear()

        self.match(self.team1, self.team2)
        self.match(self.team3, self.team4)

        self.match(self.team1, self.team3)
        self.match(self.team2, self.team4)

        self.match(self.team1, self.team4)
        self.match(self.team2, self.team3)

    def printScore(self):
        print(f'\n===== GRUPO {self.groupID} =====\n')

        classificacao = self.get_classification()

        for posicao, team in enumerate(classificacao, start=1):

            print(
                f'{posicao:>2}º | '
                f'{team.name:<15} | '
                f'Pts: {team.points:<2} | '
                f'SG: {team.saldo:<2} | '
                f'GM: {team.gm:<2} | '
                f'GS: {team.gs:<2}'
            )

        print(f"\n===== JOGOS DO GRUPO {self.groupID} =====\n")

        for match in self.matches:
            print(match)

    def get_classification(self):
        teams = [
            self.team1,
            self.team2,
            self.team3,
            self.team4
        ]

        return sorted(
            teams,
            key=lambda t: (
                t.points,
                t.saldo,
                t.gm,
                t.rank
            ),
            reverse=True
        )

