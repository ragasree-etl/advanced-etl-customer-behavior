
import pandas as pd
from datetime import datetime

# Load datasets
df_web = pd.read_csv("data/raw_web_activity.csv")
df_support = pd.read_csv("data/raw_support_logs.csv")
df_tx = pd.read_csv("data/raw_transactions.csv")

# Preprocess dates
df_web["Session_Date"] = pd.to_datetime(df_web["Session_Date"])
df_support["Ticket_Date"] = pd.to_datetime(df_support["Ticket_Date"])
df_tx["Transaction_Date"] = pd.to_datetime(df_tx["Transaction_Date"])

# Aggregate web data
web_agg = df_web.groupby("User_ID").agg({
    "Page_Views": "sum",
    "Clicks": "sum",
    "Session_Date": "count"
}).rename(columns={"Session_Date": "Web_Sessions"}).reset_index()

# Aggregate support data
support_agg = df_support.groupby("User_ID").agg({
    "Resolution_Time_Hours": "mean",
    "Resolved": lambda x: (x == "Yes").sum()
}).rename(columns={"Resolution_Time_Hours": "Avg_Resolution_Time", "Resolved": "Tickets_Resolved"}).reset_index()

# Aggregate transaction data
tx_agg = df_tx.groupby("User_ID").agg({
    "Amount": "sum",
    "Transaction_Date": "count"
}).rename(columns={"Amount": "Total_Spent", "Transaction_Date": "Transactions"}).reset_index()

# Merge all
df_merged = web_agg.merge(support_agg, on="User_ID", how="outer").merge(tx_agg, on="User_ID", how="outer").fillna(0)

# Scoring logic
df_merged["Engagement_Score"] = df_merged["Page_Views"] + df_merged["Clicks"] + df_merged["Web_Sessions"]
df_merged["Churn_Risk"] = df_merged.apply(lambda x: "High" if x["Engagement_Score"] < 10 and x["Tickets_Resolved"] == 0 else "Medium" if x["Engagement_Score"] < 20 else "Low", axis=1)

# Save output
df_merged.to_csv("data/curated_behavior_model.csv", index=False)
print("ETL pipeline completed and saved as 'curated_behavior_model.csv'")
