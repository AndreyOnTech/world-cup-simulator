import json
import os
import streamlit as st
from pathlib import Path
from PIL import Image, ImageOps

BASE_DIR = Path(__file__).resolve().parent.parent
resultado_file = BASE_DIR / "sistema_elo/resultado.json"

FLAG_WIDTH = 100
FLAG_HEIGHT = 60


def load_flag_image(flag_code):
    flag_path = BASE_DIR / "bandeira" / f"{flag_code}.png"

    if not flag_path.exists():
        return None

    with Image.open(flag_path) as flag_image:
        flag_image = ImageOps.contain(
            flag_image.convert("RGBA"),
            (FLAG_WIDTH, FLAG_HEIGHT)
        )

        canvas = Image.new(
            "RGBA",
            (FLAG_WIDTH, FLAG_HEIGHT),
            (255, 255, 255, 0)
        )

        offset = (
            (FLAG_WIDTH - flag_image.width) // 2,
            (FLAG_HEIGHT - flag_image.height) // 2,
        )

        canvas.paste(flag_image, offset, flag_image)

    return canvas


with open(resultado_file, "r", encoding="utf-8") as f:
    data = json.load(f)

st.set_page_config(layout="wide")

st.title("🏆 Simulação da Copa do Mundo")

groups = {
    "A": ["Mexico", "South Africa", "Korea Republic", "Czechia"],
    "B": ["Canada", "Bosnia and Herzegovina", "Qatar", "Switzerland"],
    "C": ["Brazil", "Morocco", "Haiti", "Scotland"],
    "D": ["USA", "Paraguay", "Australia", "Türkiye"],
    "E": ["Germany", "Curaçao", "Côte d'Ivoire", "Ecuador"],
    "F": ["Netherlands", "Japan", "Sweden", "Tunisia"],
    "G": ["Belgium", "Egypt", "IR Iran", "New Zealand"],
    "H": ["Spain", "Cabo Verde", "Saudi Arabia", "Uruguay"],
    "I": ["France", "Senegal", "Iraq", "Norway"],
    "J": ["Argentina", "Algeria", "Austria", "Jordan"],
    "K": ["Portugal", "Congo DR", "Uzbekistan", "Colombia"],
    "L": ["England", "Croatia", "Ghana", "Panama"]
}

# Descobre os terceiros colocados de todos os grupos
terceiros = []

for group_name, teams in groups.items():

    ranking = sorted(
        teams,
        key=lambda team: data[team].get("classificado", 0),
        reverse=True
    )

    terceiros.append(
        (
            ranking[2],
            data[ranking[2]].get("classificado", 0)
        )
    )

# Melhores 8 terceiros
melhores_terceiros = {
    team
    for team, _ in sorted(
        terceiros,
        key=lambda x: x[1],
        reverse=True
    )[:8]
}

st.header("📊 Probabilidade de Classificação por Grupo")

for group_name, teams in groups.items():

    ranking = sorted(
        teams,
        key=lambda team: data[team].get("classificado", 0),
        reverse=True
    )

    primeiro = ranking[0]
    segundo = ranking[1]

    st.subheader(f"Grupo {group_name}")

    cols = st.columns(4)

    for col, team in zip(cols, ranking):

        stats = data[team]

        classificacao = stats.get("classificado", 0)

        if team == primeiro:
            cor = "#90EE90"      # verde forte
        elif team == segundo:
            cor = "#C8F7C5"      # verde claro
        elif team in melhores_terceiros:
            cor = "#FFF3CD"      # amarelo
        else:
            cor = "#F8F9FA"      # neutro

        with col:

            with st.container():

                st.markdown(
                    f"""
                    <div style="
                        background-color:{cor};
                        padding:10px;
                        border-radius:8px;
                        border:1px solid #cccccc;
                        text-align:center;
                    ">
                    """,
                    unsafe_allow_html=True
                )

                flag_image = load_flag_image(
                    stats["FlagCode"]
                )

                if flag_image is not None:
                    st.image(flag_image, width=FLAG_WIDTH)

                st.markdown(f"**{team}**")

                st.write(
                    f"Classificou: {classificacao:,} vezes"
                )

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True
                )

    st.divider()



times = sorted(
    data.items(),
    key=lambda x: (
        x[1].get("1", 0),
        x[1].get("2", 0),
        x[1].get("4", 0),
        x[1].get("8", 0),
        x[1].get("16", 0),
        x[1].get("32", 0)
    ),
    reverse=True
)

st.header("🏅 Ranking Geral")

for i in range(0, len(times), 4):

    cols = st.columns(4)

    for col, (country, stats) in zip(cols, times[i:i+4]):

        with col:

            with st.container(border=True):

                flag_image = load_flag_image(
                    stats["FlagCode"]
                )

                if flag_image is not None:
                    st.image(flag_image, width=FLAG_WIDTH)

                st.markdown(
                    f"### {country}"
                )

                st.caption(
                    f"Ranking FIFA: {stats['Rank']}"
                )

                st.write(
                    f"🏆 Campeão: {stats.get('1', 0)}"
                )

                st.write(
                    f"🥈 Vice: {stats.get('2', 0)}"
                )

                st.write(
                    f"🥉 Semifinal: {stats.get('4', 0)}"
                )

                st.write(
                    f"🎯 Quartas: {stats.get('8', 0)}"
                )

                st.write(
                    f"⚽ Oitavas: {stats.get('16', 0)}"
                )

                st.write(
                    f"📋 Classificado: {stats.get('32', 0)}"
                )