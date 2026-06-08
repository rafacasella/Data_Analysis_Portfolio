# 📊 Data Analysis Portfolio

Welcome to my project portfolio! This repository brings together end-to-end solutions in data analysis, data engineering, and process automation using **Python** and **SQL**. 

The goal of this repository is to demonstrate the practical application of data to generate business insights and optimize daily routines.

---

## 📂 Featured Projects

### 1. 📉 Banking Churn Analysis & Prediction (Statistical Modeling)
* **Where to Find:** `/Churn_Analysis` folder
* **Description:** Predictive investigation utilizing a Logistic Regression model to identify and quantify the impact of operational, contractual, and demographic factors on customer cancellation (dataset featuring over 64,000 records).
* **Technologies:** Python (`pandas`, `statsmodels`, `psycopg2`), Database (`PostgreSQL`), and Jupyter Notebook.
* **Key Insights:** 
  * **Support Friction:** Each additional call made to customer support increases the likelihood of customer cancellation by **39.3%**.
  * **Contractual Fragility:** Customers with Monthly contracts present a **37.8% higher** Churn risk compared to those on Annual contracts.
  * **Red Flag:** Each day of payment delay (`paymentdelays`) raises the risk of churn by **23.8%**.

### 2. 📈 Financial KPI Dashboard (KPIs_Analysis)
* **Where to Find:** `/KPIs_Analysis` folder | Link: https://kpis4cfo.streamlit.app/
* **Description:** An interactive web application focused on structuring corporate performance metrics (KPIs), engineered to support strategic decision-making through real-time monitoring of financial health and sales performance.
* **Technologies:** 
  * **Python:** Core language utilized throughout the entire project.
  * **Pandas:** Manipulation, cleaning, and advanced processing of raw data.
  * **Matplotlib/Seaborn:** Construction and styling of compelling statistical visualizations.
  * **Streamlit:** Framework for rendering the web interface and deploying the dashboard.
* **Key Insights:** 
  * **Growth Leverage:** Protecting the flagship product, prioritizing investments, and targeting traffic campaigns.
  * **Risk Mitigation:** Identifying products with extremely high operational costs that bottleneck the entire operation (stifling profit).
  * **Recovery Plan:** Adjusting the sales mix, encouraging the commercial team to focus on higher-margin products.

### 3. 💼 Dynamic Stock Portfolio Tracker
* **Where to Find:** `/Stock_Portfolio` folder | Link: https://rafacasella-portifolio-an-portifolioacoesportifolioacoes-ydwzap.streamlit.app/
* **Description:** A tool for financial asset analysis featuring return normalization and direct performance comparison against the Bovespa Index (IBOV) benchmark.

---

## 🛠️ Tech Stack & Tools

* **Languages:** Python, SQL (PostgreSQL)
* **Data Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Web Apps:** Streamlit
* **Development IDE:** PyCharm
* **Version Control:** Git & GitHub Desktop
* **Security:** Local credential management via `python-dotenv`

---

## 🔒 Applied Security Best Practices

This repository adheres to strict data security standards for production environments:
* **Credential Masking:** No passwords or database connection strings are exposed in the public code. All sensitive variables are dynamically injected via a local `.env` file.
* **Clean Versioning:** The `.gitignore` file is rigorously configured to prevent the accidental upload of virtual environment dependencies (`.venv/`), cryptographic keys, or temporary local databases.

---
