# 💼 Dynamic Stock Portfolio Tracker

## 📝 Description
This project is an interactive web application designed for investors and financial analysts. The tool enables the analysis of assets from the Brazilian stock exchange, applying return normalization for a fair performance comparison and generating a direct matchup against the country's primary market benchmark, the Bovespa Index (IBOV).

## 🔗 Online Demo
The application is deployed and ready for cloud use:
👉 [Access the Dynamic Stock Portfolio Tracker on Streamlit](https://rafacasella-portifolio-an-portifolioacoesportifolioacoes-ydwzap.streamlit.app/)

## 🛠️ Tech Stack
* **Python** (Core language)
* **Streamlit** (Web interface construction and interactive dashboard)
* **Pandas** / **NumPy** (Data manipulation, return calculation, and normalization)
* **yfinance** (Integration and consumption of historical financial data via Yahoo Finance API)
* **Plotly** / **Matplotlib** (Dynamic performance chart visualizations)

## 📁 File Structure
* `PortifolioAcoes.py`: Main script that renders the Streamlit application.
* `tickers.csv`: Support file containing the list and symbols of monitored assets.
* `requirements.txt`: Dependencies and libraries required to run the ecosystem.

## 🚀 How to Run Locally

1. Navigate to the project folder in your terminal:
   ```bash
   cd PortifolioAcoes
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the local Streamlit server:
   ```bash
   streamlit run PortifolioAcoes.py
   ```

---
📌 *This project is part of my Data Analysis Portfolio.*
