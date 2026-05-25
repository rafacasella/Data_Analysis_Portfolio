# 📊 Portfólio de Análise de Dados & Automação

Bem-vindo ao meu portfólio de projetos! Aqui estão reunidas soluções completas de análise de dados, engenharia de dados e automação de processos utilizando **Python** e **SQL**. 

O objetivo deste repositório é demonstrar a aplicação prática de dados para a geração de insights de negócios e otimização de rotinas diárias.

---

## 📂 Projetos em Destaque

### 1. 📉 Análise e Predição de Churn de Dados Bancários (Modelo Estatístico)
* **Onde encontrar:** Pasta `/Churn_Analysis`
* **Descrição:** Investigação preditiva utilizando um modelo de Regressão Logística para identificar e quantificar o impacto dos fatores operacionais, contratuais e demográficos no cancelamento de clientes (dataset com mais de 64 mil registros).
* **Tecnologias:** Python (`pandas`, `statsmodels`, `psycopg2`), Banco de Dados (`PostgreSQL`) e Jupyter Notebook.
* **Principais Insights:** 
  * **Atrito no Suporte:** Cada ligação adicional realizada para o suporte aumenta as chances de cancelamento do cliente em **39.3%**.
  * **Fragilidade Contratual:** Clientes com contratos do tipo Mensal possuem um risco de Churn **37.8% maior** em relação aos contratos Anuais.
  * **Sinal de Alerta:** Cada dia de atraso no pagamento do cliente (`paymentdelays`) eleva o risco de perda em **23.8%**.

### 2. 📈 Painel de Indicadores Financeiros (AnaliseKPIS)
* **Onde encontrar:** Pasta `/AnaliseKPIS`  link: https://kpis4cfo.streamlit.app/
* **Descrição:** O Painel de Indicadores Financeiros é uma aplicação interativa focada na estruturação de métricas de desempenho corporativo (KPIs), projetada para apoiar decisões estratégicas através do monitoramento em tempo real da saúde financeira e da performance de vendas.
* **Tecnologias:** 
* * **Python:** Linguagem base utilizada em todo o projeto
* * **Pandas:** Manipulação, limpeza e tratamento avançado dos dados brutos
* * **MatplotLib/Seaborn:** Construção e estilização de visualizações estatísticas atraentes
* * **Streamlit:** Framework para renderização da interface web e deploy do painel
* **Principais Insights:** 
  * **Alavancagem de Crescimento:** Protegendo o produto estrela, priorizando investimentos e direcionando campanhas de tráfego
  * **Mitigação de Riscos:** Identificação dos produtos com altíssimo custo operacional que gargala toda operação (estrangulando lucro)
  * **Plano de Recuperação:** Alteração do mix de vendas, incentivando o time comercial a focar em produtos com maiores margens.

### 3. 💼 Portfólio de Ações Dinâmico
* **Onde encontrar:** Pasta `/PortifolioAcoes` link: https://rafacasella-portifolio-an-portifolioacoesportifolioacoes-ydwzap.streamlit.app/
* **Descrição:** Ferramenta para análise de ativos financeiros com normalização de retornos e comparação direta com o benchmark do Índice Bovespa (IBOV).

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagens:** Python, SQL (PostgreSQL)
* **Análise de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn
* **Apps:** Streamlit
* **IDE de Desenvolvimento:** PyCharm
* **Controle de Versão:** Git & GitHub Desktop
* **Segurança:** Gestão de credenciais locais via `python-dotenv`

---

## 🔒 Boas Práticas de Segurança Aplicadas

Este repositório segue padrões rígidos de segurança de dados para ambientes de produção:
* **Mascaramento de Credenciais:** Nenhuma senha ou string de conexão com bancos de dados é exposta no código público. Todas as variáveis sensíveis são injetadas dinamicamente via arquivo `.env` local.
* **Versionamento Limpo:** O arquivo `.gitignore` foi rigorosamente configurado para impedir o envio acidental de dependências de ambientes virtuais (`.venv/`), chaves criptográficas ou bases de dados locais temporárias.

---
