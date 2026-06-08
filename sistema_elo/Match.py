import math
import random

vitorias = [
    (1, 0),
    (2, 1),
    (3, 1),
    (3, 0)
]

empates = [
    (0, 0),
    (1, 1),
    (2, 2)
]

def play_match(team1, team2):

    expectativa_time1 = 1 / (
        1 + math.pow(10, (team2.pointsFifa - team1.pointsFifa) / 600)
    )

    expectativa_time2 = 1 - expectativa_time1
    diferenca = abs(team1.pointsFifa - team2.pointsFifa)

    if diferenca <= 50:
        empate = 0.30
    elif diferenca <= 100:
        empate = 0.25
    elif diferenca <= 200:
        empate = 0.20
    elif diferenca <= 300:
        empate = 0.15
    else:
        empate = 0.10

    vitoria_time1 = expectativa_time1 * (1 - empate)
    vitoria_time2 = expectativa_time2 * (1 - empate)

    resultado = random.random()

    if resultado < vitoria_time1:
        gols1, gols2 = random.choice(vitorias)

        return (
            "TIME1",
            gols1,
            gols2
        )

    elif resultado < (vitoria_time1 + empate):
        gols1, gols2 = random.choice(empates)

        return (
            "EMPATE",
            gols1,
            gols2
        )

    else:
        gols2, gols1 = random.choice(vitorias)

        return (
            "TIME2",
            gols1,
            gols2
        )


def knockout_match(team1, team2):

    resultado, _, _ = play_match(team1, team2)

    if resultado == "TIME1":
        return team1

    if resultado == "TIME2":
        return team2

    # empate -> pênaltis
    return random.choice([team1, team2])


def knockout_round(addClassification, fase, teams):

    classificados = []

    random.shuffle(teams)

    for i in range(0, len(teams), 2):

        team1 = teams[i]
        team2 = teams[i + 1]

        vencedor = knockout_match(team1, team2)

        """print(
            f'{team1.name} x {team2.name} -> '
            f'{vencedor.name}'
        )"""


        addClassification(fase, team2.name if team1.name == vencedor.name else team1.name)
        classificados.append(vencedor)

    return classificados

