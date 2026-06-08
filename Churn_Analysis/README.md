# 📉 Banking Churn Analysis & Prediction

### 📌 About the Project
This project conducts an in-depth predictive and statistical analysis of customer churn utilizing historical data from a financial institution. The primary objective is to identify behavioral, operational, and demographic triggers that lead a customer to cancel their services, enabling business teams to take preventive action.

The project evolved from a descriptive SQL analysis into a robust **Logistic Regression Model** in Python, allowing for the quantification of the actual impact each variable has on the likelihood of cancellation.

---

### 🛠️ Tech Stack & Tools
* **Database:** PostgreSQL (Storage, structuring, and raw data extraction).
* **Language:** Python 3.x (Data analysis and statistical modeling).
* **Core Libraries:** `pandas`, `psycopg2`, `statsmodels`, `seaborn`, and `matplotlib`.
* **Security:** `python-dotenv` for secure database credential management.

---

### 📁 Repository Structure
* 📂 `Churn_Analysis/`
  * 📄 `Churn_Analysis.ipynb`: Jupyter Notebook containing feature engineering, data processing, and the regression model.
  * 📄 `churn.sql`: Structured script with data and queries for loading into PostgreSQL.
  * 🖼️ `impacto_percentual_churn.png`: Explanatory chart illustrating churn levers.
* 📄 `.env.example`: Template for configuring database environment variables.
* 📄 `.gitignore` & `.gitattributes`: Global version control and line ending configurations.
* 📄 `requirements.txt`: File containing the exact project dependencies.

📌 *This project is part of my Data Analysis and Data Science Portfolio.*
