from Group import Group
from Match import knockout_round

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
teams_file = BASE_DIR / "teams.json"

with open(teams_file, "r", encoding="utf-8") as f:
    dados = json.load(f)

dados = dados['TeamsData']

groups = [
    Group(dados, "A", "Mexico", "South Africa", "Korea Republic", "Czechia"),
    Group(dados, "B", "Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"),
    Group(dados, "C", "Brazil", "Morocco", "Haiti", "Scotland"),
    Group(dados, "D", "USA", "Paraguay", "Australia", "Türkiye"),
    Group(dados, "E", "Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"),
    Group(dados, "F", "Netherlands", "Japan", "Sweden", "Tunisia"),
    Group(dados, "G", "Belgium", "Egypt", "IR Iran", "New Zealand"),
    Group(dados, "H", "Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"),
    Group(dados, "I", "France", "Senegal", "Iraq", "Norway"),
    Group(dados, "J", "Argentina", "Algeria", "Austria", "Jordan"),
    Group(dados, "K", "Portugal", "Congo DR", "Uzbekistan", "Colombia"),
    Group(dados, "L", "England", "Croatia", "Ghana", "Panama")
]

def addClassification(fase, team):
    dados[team][fase] = dados[team].get(fase, 0) + 1

for i in range(1):

    primeiros = []
    segundos = []
    terceiros_colocados = []

    for group in groups:
        group.group_exec()

        classificacao = group.get_classification()

        primeiros.append(classificacao[0])
        segundos.append(classificacao[1])
        terceiros_colocados.append(classificacao[2])

    terceiro_sort = sorted(
                terceiros_colocados,
                key=lambda t: (
                    t.points,
                    t.saldo,
                    t.gm,
                    t.rank
                ),
                reverse=True
            )

    melhores_terceiros = []

    for posicao, team in enumerate(terceiro_sort[:8], start=1):
        melhores_terceiros.append(team)

    classificados = (
        primeiros +
        segundos +
        melhores_terceiros
    )

    classificados16 = knockout_round(addClassification, '32', classificados)
    classificados8 = knockout_round(addClassification, '16', classificados16)
    classificados4 = knockout_round(addClassification, '8', classificados8)
    classificados2 = knockout_round(addClassification, '4', classificados4)
    classificados1 = knockout_round(addClassification, '2', classificados2)


    print(len(classificados1))
    print(f'Campeão {classificados1[0].name}')
    addClassification("1", classificados1[0].name)


resultado_file = BASE_DIR / "sistema_elo/resultado.json"
with open(resultado_file, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)