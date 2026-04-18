import os
import pandas as pd
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Retail Analytics Dashboard", layout="wide")

st.title("📊 Retail Sales Forecasting & Inventory Dashboard")

# ---------------- PATH SETUP ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

forecast_path = os.path.join(BASE_DIR, "outputs", "forecasts.csv")
inventory_path = os.path.join(BASE_DIR, "outputs", "inventory_plan.csv")
metrics_path = os.path.join(BASE_DIR, "outputs", "metrics.csv")

# ---------------- FILE CHECK ----------------
if not os.path.exists(forecast_path):
    st.error("⚠️ Forecast file not found. Please run main.py first.")
    st.stop()

# ---------------- LOAD DATA ----------------
df = pd.read_csv(forecast_path)

inv = pd.read_csv(inventory_path) if os.path.exists(inventory_path) else None
metrics = pd.read_csv(metrics_path) if os.path.exists(metrics_path) else None

# ---------------- SIDEBAR FILTER ----------------
st.sidebar.header("🔍 Filters")
product = st.sidebar.selectbox("Select Product", df['product'].unique())

filtered = df[df['product'] == product]

# ---------------- KPIs ----------------
st.subheader("📌 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Sales", round(filtered['sales'].dropna().mean(), 2))
col2.metric("Avg Forecast", round(filtered['forecast'].dropna().mean(), 2))
col3.metric("Peak Forecast", round(filtered['forecast'].max(), 2))

# ---------------- CHART ----------------
st.subheader("📈 Sales vs Forecast")

chart_df = filtered[['sales', 'forecast']].dropna()
st.line_chart(chart_df)

# ---------------- INVENTORY ----------------
if inv is not None:
    st.subheader("📦 Inventory Recommendation")

    inv_filtered = inv[inv['product'] == product]
    st.dataframe(inv_filtered)

# ---------------- METRICS ----------------
if metrics is not None:
    st.subheader("📊 Model Performance")

    st.dataframe(metrics)

    selected_metrics = metrics[metrics['product'] == product]

    if not selected_metrics.empty:
        m1, m2, m3 = st.columns(3)

        mae = selected_metrics["MAE"].values[0]
        rmse = selected_metrics["RMSE"].values[0]
        mape = selected_metrics["MAPE (%)"].values[0]

        m1.metric("MAE", round(mae, 2))
        m2.metric("RMSE", round(rmse, 2))
        m3.metric("MAPE (%)", round(mape, 2))

# ---------------- INSIGHTS ----------------
st.subheader("📊 Business Insights")

if filtered['forecast'].mean() > filtered['sales'].mean():
    st.success("📈 Demand is increasing → Consider stocking more")
else:
    st.warning("📉 Demand is decreasing → Avoid overstocking")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Retail Forecasting System | ARIMA + Inventory Optimization + Streamlit")