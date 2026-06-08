# World Cup Simulator

PT-BR | [English](#english)

Simulador de Copa do Mundo baseado em ratings no estilo Elo e nos pontos do ranking masculino da FIFA.

Este projeto foi criado para experimentar cenarios de torneio, gerar probabilidades de campanha e publicar conteudo no ecossistema Andrey On Tech.

Ranking de referencia utilizado neste projeto:
https://inside.fifa.com/fifa-world-ranking/men

Ultima referencia registrada no repositorio: 02/06/2026.

## PT-BR

### Visao geral

O projeto simula uma Copa do Mundo com 48 selecoes, distribuindo os times em 12 grupos e avancando para mata-mata com os 2 melhores de cada grupo mais os 8 melhores terceiros colocados.

O fluxo principal e:

1. `teams.json` armazena ranking FIFA, pontuacao e metadados das selecoes.
2. `sistema_elo/Simulator.py` executa a simulacao e grava os resultados agregados em `sistema_elo/resultado.json`.
3. `sistema_elo/App.py` le esse arquivo e exibe o painel em Streamlit.

Para a explicacao tecnica do modelo, veja [sistema_elo/README.md](sistema_elo/README.md).

### Recursos

- Simulacao de fase de grupos e mata-mata.
- Uso de expectativa de resultado baseada em diferenca de pontuacao.
- Interface simples em Streamlit para visualizar o desempenho de cada selecao.
- Base de dados em JSON, facil de atualizar para novos rankings.

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

1. `teams.json` stores ranking points, rank position, and team metadata.
2. `sistema_elo/Simulator.py` runs the tournament simulation and writes aggregated results to `sistema_elo/resultado.json`.
3. `sistema_elo/App.py` reads that file and renders the dashboard with Streamlit.

For the technical explanation of the model, see [sistema_elo/README.md](sistema_elo/README.md).

### Features

- Group stage and knockout stage simulation.
- Match expectation driven by rating differences.
- Streamlit dashboard for browsing each team's outcomes.
- JSON-based dataset that is easy to refresh with new FIFA rankings.

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
