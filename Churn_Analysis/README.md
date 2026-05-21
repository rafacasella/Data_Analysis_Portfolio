# 📉 Análise e Predição de Churn Bancário

### 📌 Sobre o Projeto
Este projeto realiza uma análise preditiva e estatística aprofundada sobre a evasão de clientes (*churn*) utilizando dados históricos de uma instituição financeira. O objetivo principal é identificar os gatilhos comportamentais, operacionais e demográficos que levam um cliente a cancelar seus serviços, permitindo que a equipe de negócios atue de forma preventiva.

O projeto foi evoluído de uma análise descritiva em SQL para um **Modelo de Regressão Logística** robusto em Python, permitindo quantificar o impacto real de cada variável na chance de cancelamento.

---

### 🛠️ Tecnologias e Ferramentas
* **Banco de Dados:** PostgreSQL (Armazenamento, estruturação e extração dos dados brutos).
* **Linguagem:** Python 3.x (Análise de dados e modelagem estatística).
* **Bibliotecas Principais:** `pandas`, `psycopg2`, `statsmodels`, `seaborn` e `matplotlib`.
* **Segurança:** `python-dotenv` para gerenciamento seguro de credenciais de banco de dados.

---

### 📁 Estrutura do Repositório
* 📂 `Churn_Analysis/`
  * 📄 `Churn_Analysis.ipynb`: Notebook Jupyter contendo a engenharia de recursos, tratamento de dados e o modelo de regressão.
  * 📄 `churn.sql`: Script estruturado com os dados e consultas para carga no PostgreSQL.
  * 🖼️ `impacto_percentual_churn.png`: Gráfico explicativo das alavancas de Churn.
* 📄 `.env.example`: Modelo de configuração das variáveis de ambiente do banco de dados.
* 📄 `.gitignore` & `.gitattributes`: Configurações globais de versionamento e quebras de linha.
* 📄 `requirements.txt`: Arquivo com as dependências exatas do projeto.

📌 *Este projeto faz parte do meu Portfólio de Análise e Ciência de Dados.*