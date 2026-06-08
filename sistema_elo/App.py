import json
import os
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
resultado_file = BASE_DIR / "sistema_elo/resultado.json"

with open(resultado_file, "r", encoding="utf-8") as f:
    data = json.load(f)

st.set_page_config(layout="wide")

st.title("🏆 Simulação da Copa do Mundo")

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

for i in range(0, len(times), 4):

    cols = st.columns(4)

    for col, (country, stats) in zip(cols, times[i:i+4]):

        with col:

            with st.container(border=True):

                flag_file = f"bandeira/{stats['FlagCode']}.png"

                if os.path.exists(flag_file):
                    st.image(flag_file, width=100)

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