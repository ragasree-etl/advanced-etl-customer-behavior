# Advanced ETL Project – Customer Behavior Analytics

## 📌 Overview
This project demonstrates a complete ETL pipeline that integrates customer web activity, support tickets, and transaction data to build an engagement model and churn risk classification. It's designed for modern data teams working with multi-source ingestion and behavioral analytics.

## 💡 Key Features
- Multi-source ingestion: web, support, and transaction logs
- Data aggregation, scoring, and enrichment with Python
- Customer engagement scoring and churn risk tagging
- Output dataset ready for Snowflake, ML models, and dashboards
- Power BI/Tableau-style preview dashboard

## 🛠️ Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Data warehouse-ready output (Snowflake-compatible)
- Power BI / Tableau for dashboarding
- Jupyter for exploratory data transformation

## 📂 Project Structure
```
advanced_etl_customer_behavior/
├── data/
│   ├── raw_web_activity.csv
│   ├── raw_support_logs.csv
│   ├── raw_transactions.csv
│   └── curated_behavior_model.csv
├── scripts/
│   └── etl_pipeline_customer_behavior.py
├── notebooks/
│   └── etl_pipeline_customer_behavior.ipynb
├── visuals/
│   └── behavior_dashboard_preview.png
├── docs/
│   └── README.md
```

## 🚀 How to Use
1. Run the ETL pipeline (`.py` or notebook) to process all datasets
2. Analyze the output: `curated_behavior_model.csv`
3. Use the dashboard as a BI starting point in Power BI/Tableau
4. Extend churn risk logic or connect to Snowflake schema

---

🔍 Built for showcasing ETL automation, data storytelling, and behavioral analytics.

