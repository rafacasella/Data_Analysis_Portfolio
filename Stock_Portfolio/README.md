# 💼 Portfólio de Ações Dinâmico

## 📝 Descrição
Este projeto é uma aplicação web interativa desenvolvida para investidores e analistas financeiros. A ferramenta permite realizar a análise de ativos da bolsa de valores brasileira, aplicando a normalização de retornos para uma comparação justa de desempenho e gerando um confronto direto contra o principal benchmark do mercado nacional, o Índice Bovespa (IBOV).

## 🔗 Demonstração Online
O aplicativo está publicado e pronto para uso na nuvem:
👉 [Acesse o Portfólio de Ações Dinâmico no Streamlit](https://rafacasella-portifolio-an-portifolioacoesportifolioacoes-ydwzap.streamlit.app/)

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem base)
* **Streamlit** (Construção da interface web e painel interativo)
* **Pandas** / **NumPy** (Manipulação, cálculo de retornos e normalização de dados)
* **yfinance** (Integração e consumo de dados financeiros históricos da API do Yahoo Finance)
* **Plotly** / **Matplotlib** (Visualizações gráficas dinâmicas de performance)

## 📁 Estrutura de Arquivos
* `PortifolioAcoes.py`: Script principal que renderiza a aplicação no Streamlit.
* `tickers.csv`: Arquivo de apoio contendo a lista e códigos dos ativos monitorados.
* `requirements.txt`: Dependências e bibliotecas necessárias para a execução do ecossistema.

## 🚀 Como Executar Localmente

1. Navegue até a pasta do projeto no seu terminal:
   ```bash
   cd PortifolioAcoes
   ```
2. Instale as bibliotecas necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicie o servidor local do Streamlit:
   ```bash
   streamlit run PortifolioAcoes.py
   ```

---
📌 *Este projeto faz parte do meu Portfólio de Análise de Dados.*