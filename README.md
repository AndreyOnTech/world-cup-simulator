# World Cup Simulator

Follow us on Youtube: https://youtu.be/jcFr0PJAeOU


PT-BR | [English](#english)

Simulador de Copa do Mundo baseado em ratings no estilo Elo e nos pontos do ranking masculino da FIFA.

Este projeto foi criado para experimentar cenarios de torneio, gerar probabilidades de campanha e publicar conteudo no ecossistema Andrey On Tech.

Ranking de referencia utilizado neste projeto:
https://inside.fifa.com/fifa-world-ranking/men

Ultima referencia registrada no repositorio: 02/06/2026.

## Grupos / Groups

Passe o mouse sobre cada bandeira para ver o nome da selecao, se o renderizador suportar `title`. Hover over each flag to see the team name when the renderer supports `title`.

| Grupo | Time 1 | Time 2 | Time 3 | Time 4 |
| --- | --- | --- | --- | --- |
| A | <img src="bandeira/mx.png" alt="Mexico" title="Mexico" width="22" /> | <img src="bandeira/za.png" alt="South Africa" title="South Africa" width="22" /> | <img src="bandeira/kr.png" alt="Korea Republic" title="Korea Republic" width="22" /> | <img src="bandeira/cz.png" alt="Czechia" title="Czechia" width="22" /> |
| B | <img src="bandeira/ca.png" alt="Canada" title="Canada" width="22" /> | <img src="bandeira/ba.png" alt="Bosnia and Herzegovina" title="Bosnia and Herzegovina" width="22" /> | <img src="bandeira/qa.png" alt="Qatar" title="Qatar" width="22" /> | <img src="bandeira/ch.png" alt="Switzerland" title="Switzerland" width="22" /> |
| C | <img src="bandeira/br.png" alt="Brazil" title="Brazil" width="22" /> | <img src="bandeira/ma.png" alt="Morocco" title="Morocco" width="22" /> | <img src="bandeira/ht.png" alt="Haiti" title="Haiti" width="22" /> | <img src="bandeira/gb-sct.png" alt="Scotland" title="Scotland" width="22" /> |
| D | <img src="bandeira/us.png" alt="USA" title="USA" width="22" /> | <img src="bandeira/py.png" alt="Paraguay" title="Paraguay" width="22" /> | <img src="bandeira/au.png" alt="Australia" title="Australia" width="22" /> | <img src="bandeira/tr.png" alt="Türkiye" title="Türkiye" width="22" /> |
| E | <img src="bandeira/de.png" alt="Germany" title="Germany" width="22" /> | <img src="bandeira/cw.png" alt="Curaçao" title="Curaçao" width="22" /> | <img src="bandeira/ci.png" alt="Côte d'Ivoire" title="Côte d'Ivoire" width="22" /> | <img src="bandeira/ec.png" alt="Ecuador" title="Ecuador" width="22" /> |
| F | <img src="bandeira/nl.png" alt="Netherlands" title="Netherlands" width="22" /> | <img src="bandeira/jp.png" alt="Japan" title="Japan" width="22" /> | <img src="bandeira/se.png" alt="Sweden" title="Sweden" width="22" /> | <img src="bandeira/tn.png" alt="Tunisia" title="Tunisia" width="22" /> |
| G | <img src="bandeira/be.png" alt="Belgium" title="Belgium" width="22" /> | <img src="bandeira/eg.png" alt="Egypt" title="Egypt" width="22" /> | <img src="bandeira/ir.png" alt="IR Iran" title="IR Iran" width="22" /> | <img src="bandeira/nz.png" alt="New Zealand" title="New Zealand" width="22" /> |
| H | <img src="bandeira/es.png" alt="Spain" title="Spain" width="22" /> | <img src="bandeira/cv.png" alt="Cabo Verde" title="Cabo Verde" width="22" /> | <img src="bandeira/sa.png" alt="Saudi Arabia" title="Saudi Arabia" width="22" /> | <img src="bandeira/uy.png" alt="Uruguay" title="Uruguay" width="22" /> |
| I | <img src="bandeira/fr.png" alt="France" title="France" width="22" /> | <img src="bandeira/sn.png" alt="Senegal" title="Senegal" width="22" /> | <img src="bandeira/iq.png" alt="Iraq" title="Iraq" width="22" /> | <img src="bandeira/no.png" alt="Norway" title="Norway" width="22" /> |
| J | <img src="bandeira/ar.png" alt="Argentina" title="Argentina" width="22" /> | <img src="bandeira/dz.png" alt="Algeria" title="Algeria" width="22" /> | <img src="bandeira/at.png" alt="Austria" title="Austria" width="22" /> | <img src="bandeira/jo.png" alt="Jordan" title="Jordan" width="22" /> |
| K | <img src="bandeira/pt.png" alt="Portugal" title="Portugal" width="22" /> | <img src="bandeira/cd.png" alt="Congo DR" title="Congo DR" width="22" /> | <img src="bandeira/uz.png" alt="Uzbekistan" title="Uzbekistan" width="22" /> | <img src="bandeira/co.png" alt="Colombia" title="Colombia" width="22" /> |
| L | <img src="bandeira/gb-eng.png" alt="England" title="England" width="22" /> | <img src="bandeira/hr.png" alt="Croatia" title="Croatia" width="22" /> | <img src="bandeira/gh.png" alt="Ghana" title="Ghana" width="22" /> | <img src="bandeira/pa.png" alt="Panama" title="Panama" width="22" /> |

## PT-BR

### Visao geral

O projeto simula uma Copa do Mundo com 48 selecoes, distribuindo os times em 12 grupos e avancando para mata-mata com os 2 melhores de cada grupo mais os 8 melhores terceiros colocados.

O fluxo principal e:

1. `teams.json` armazena ranking FIFA, pontuacao e metadados apenas das 48 selecoes presentes no torneio atual.
2. `sistema_elo/Simulator.py` executa a simulacao e grava os resultados agregados em `sistema_elo/resultado.json`.
3. `sistema_elo/App.py` le esse arquivo e exibe o painel em Streamlit.

Para a explicacao tecnica do modelo, veja [sistema_elo/README.md](sistema_elo/README.md).

### Recursos

- Simulacao de fase de grupos e mata-mata.
- Uso de expectativa de resultado baseada em diferenca de pontuacao.
- Interface simples em Streamlit para visualizar o desempenho de cada selecao.
- Base de dados em JSON enxuta, contendo apenas as 48 selecoes do torneio atual.

### Estrutura do projeto

```text
world-cup-simulator/
|- bandeira/             # Bandeiras usadas na interface
|- sistema_elo/
|  |- App.py             # Interface Streamlit
|  |- Simulator.py       # Motor de simulacao
|  |- Group.py           # Regras da fase de grupos
|  |- Match.py           # Probabilidades e partidas
|  |- Team.py            # Modelo de time
|  |- resultado.json     # Saida agregada das simulacoes
|- teams.json            # Dados das selecoes
|- requirements.txt      # Dependencias Python
```

### Requisitos

- Python 3.11 ou superior
- `pip`
- Ambiente virtual recomendado

### Instalacao

O arquivo `requirements.txt` ja inclui o Streamlit usado por `sistema_elo/App.py`.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Como usar

1. Gere ou atualize o arquivo de resultados:

```bash
python sistema_elo/Simulator.py
```

2. Abra a interface web:

```bash
python -m streamlit run sistema_elo/App.py
```

3. O Streamlit abrira uma URL local no navegador, normalmente `http://localhost:8501`.
4. Se o comando `streamlit` nao estiver disponivel no terminal, mantenha o ambiente virtual ativado e execute exatamente via Python, como mostrado acima.

### Observacoes

- O `resultado.json` e sobrescrito a cada nova execucao do simulador.
- No estado atual do codigo, `Simulator.py` executa uma iteracao de simulacao (`range(1)`).
- As probabilidades de empate e os placares sao modelados de forma simplificada.
- As imagens de bandeiras usadas na pasta `bandeira/` sao baseadas no servico Flagcdn: https://flagcdn.com/

### Conteudo e redes

- YouTube: [@andreyontech](https://www.youtube.com/@andreyontech)
- Twitter/X: [@andreyontech](https://x.com/andreyontech)
- Site: [andreyontech.is-a.dev](https://andreyontech.is-a.dev)

---

## English

### Overview

This project simulates a 48-team FIFA World Cup using Elo-style rating expectations derived from the FIFA men's ranking points.

The main flow is:

1. `teams.json` stores ranking points, rank position, and metadata only for the 48 teams included in the current tournament.
2. `sistema_elo/Simulator.py` runs the tournament simulation and writes aggregated results to `sistema_elo/resultado.json`.
3. `sistema_elo/App.py` reads that file and renders the dashboard with Streamlit.

For the technical explanation of the model, see [sistema_elo/README.md](sistema_elo/README.md).

### Features

- Group stage and knockout stage simulation.
- Match expectation driven by rating differences.
- Streamlit dashboard for browsing each team's outcomes.
- Lean JSON dataset containing only the 48 teams used in the current tournament.

### Project structure

```text
world-cup-simulator/
|- bandeira/             # Flag assets used by the UI
|- sistema_elo/
|  |- App.py             # Streamlit UI
|  |- Simulator.py       # Simulation engine
|  |- Group.py           # Group-stage rules
|  |- Match.py           # Match probabilities and knockout logic
|  |- Team.py            # Team model
|  |- resultado.json     # Aggregated simulation output
|- teams.json            # Team dataset
|- requirements.txt      # Python dependencies
```

### Requirements

- Python 3.11+
- `pip`
- A virtual environment is recommended

### Installation

`requirements.txt` already includes Streamlit, which is used by `sistema_elo/App.py`.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

1. Generate or refresh the simulation output:

```bash
python sistema_elo/Simulator.py
```

2. Start the web interface:

```bash
python -m streamlit run sistema_elo/App.py
```

3. Open the local Streamlit URL, usually `http://localhost:8501`.
4. If the `streamlit` command is not available in your shell, keep the virtual environment activated and run it through Python exactly as shown above.

### Notes

- `resultado.json` is overwritten every time the simulator runs.
- In the current implementation, `Simulator.py` runs a single iteration (`range(1)`).
- Draw rates and scorelines are intentionally simplified.
- The flag images stored in `bandeira/` are based on assets from Flagcdn: https://flagcdn.com/

### Creator links

- YouTube: [@andreyontech](https://www.youtube.com/@andreyontech)
- Twitter/X: [@andreyontech](https://x.com/andreyontech)
- Website: [andreyontech.is-a.dev](https://andreyontech.is-a.dev)
