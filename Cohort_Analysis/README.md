# 📉 Cohort & Banking Retention Analysis

## 📌 About the Project
This project conducts an in-depth statistical and behavioral analysis of customer retention and engagement utilizing historical data from a financial institution. The primary objective is to map the customer journey over time using a classic Cohort matrix, enabling the identification of critical periods for early churn and providing strategic inputs for business teams to maximize Customer Lifetime Value (LTV).

The project was structured around robust data processing and modeling performed directly within a SQL environment (PostgreSQL), which was subsequently integrated into Power BI for a dynamic and interactive visualization of customer decay curves.

## 🛠️ Tech Stack & Tools
* **Database:** PostgreSQL (Storage, validation, and cohort matrix modeling).
* **Query Interface:** pgAdmin 4 (Script writing, auditing functions, and query optimization).
* **Data Visualization:** Power BI Desktop (Data modeling, native connection, and interactive dashboard).
* **Language:** SQL (Extraction, missing value handling, and interval index calculation).

## 🔍 Data Engineering & SQL Queries
To optimize Power BI performance, all heavy data transformation was handled directly at the source using PostgreSQL. The logic implemented in the structured scripts follows these stages:

1. **Quality Auditing:** Creation of a custom function to check for empty values in the dataset, followed by missing value treatment.
2. **Cohort Definition:** Identification of the absolute first purchase/transaction date for each `CustomerID`, establishing the customer's fixed group.
3. **Time Interval Calculation:** Calculation of the distance in months between the current transaction and the initial cohort (Month 0: first interaction; Month 1: first subsequent month, etc.).
4. **Aggregation & Metrics:** Final consolidation counting unique active customers per period to generate the exact retention percentage.

## 📊 How to View the Project
1. The Power BI report file is available inside the `/dashboard` folder.
2. For the dashboard to function perfectly on your machine, you must open the file and change the data source credentials to point to your own PostgreSQL server.
3. *(Optional)* You can also view the dashboard's behavior using the `dashboard_final.png` or the animated `.gif` file contained within the presentation folder.

## 🗄️ Database Loading
1. Restore the retail structure and data using the file located at `data/database.sql` within your PostgreSQL instance.
2. Execute the analytical scripts from the `sql` folder using pgAdmin 4 to process and structure the final cohort view.

***
📌 *This project is part of my Data Analysis and Data Engineering Portfolio.*
