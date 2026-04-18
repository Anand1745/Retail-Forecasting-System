# 📦 Retail Sales Forecasting & Inventory Optimization System

## 🚀 Project Overview

This project is an **end-to-end retail analytics system** that forecasts product demand and optimizes inventory levels using time-series modeling and business logic.

It simulates a real-world retail environment and demonstrates how data science can be applied to improve **inventory efficiency, reduce costs, and increase profitability**.

---

## 🎯 Problem Statement

Retail businesses often face:

* ❌ Stockouts → Lost sales and customer dissatisfaction
* ❌ Overstocking → Increased storage and holding costs

---

## 💡 Solution

This system:

* 📈 Forecasts demand using **ARIMA (Time-Series Model)**
* 📦 Calculates **Safety Stock & Reorder Points**
* 📊 Evaluates model performance using **MAE, RMSE, MAPE**
* 🌐 Provides an interactive **Streamlit dashboard** for insights

---

## 🧠 Industry Relevance

Similar systems are used by companies like:

* Amazon
* Walmart
* Flipkart
* Reliance Retail

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Statsmodels (ARIMA)
* Matplotlib
* Streamlit

---

## 🏗️ Project Architecture

```text
Raw Data → Preprocessing → ARIMA Forecasting → Inventory Optimization → Dashboard
```

---

## 📁 Project Structure

```
Retail-Forecasting-System/
│
├── data/
├── src/
│   ├── generate_data.py
│   ├── data_preprocessing.py
│   ├── forecasting.py
│   ├── inventory.py
│   ├── evaluation.py
│   └── utils.py
│
├── outputs/
│   ├── forecasts.csv
│   ├── inventory_plan.csv
│   ├── metrics.csv
│   └── plots/
│
├── app/
│   └── app.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd Retail-Forecasting-System
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Step 1: Run the pipeline

```bash
python main.py
```

### Step 2: Launch dashboard

```bash
streamlit run app/app.py
```

---

## 📊 Outputs

### 📁 Generated Files

* `forecasts.csv` → Predicted demand
* `inventory_plan.csv` → Stock recommendations
* `metrics.csv` → Model performance

### 📈 Visual Outputs

* Sales vs Forecast graphs
* Residual analysis plots

---

## 📊 Dashboard Features

* 📌 KPI metrics (Sales, Forecast, Peak Demand)
* 📈 Forecast vs Actual visualization
* 📦 Inventory recommendations
* 📊 Model evaluation (MAE, RMSE, MAPE)
* 📊 Business insights

---

## 🧪 Virtual Simulation

Since real retail data is not available, this project:

* Generates synthetic multi-product sales data
* Simulates seasonality and demand variation
* Mimics real retail scenarios

---

## 💼 Business Value

* Improves demand planning
* Reduces inventory cost
* Prevents stockouts
* Supports data-driven decision making

---

## 📈 Results

* Successfully implemented ARIMA-based forecasting
* Achieved measurable accuracy using MAE, RMSE, MAPE
* Built an end-to-end analytics pipeline

---

## 🚀 Future Improvements

* Multi-store forecasting
* Price elasticity modeling
* Real-time data pipeline
* XGBoost / ML model comparison
* Power BI dashboard integration

---

## 🎓 Learning Outcomes

* Time-series forecasting (ARIMA)
* Inventory optimization techniques
* Model evaluation metrics
* Dashboard development with Streamlit
* End-to-end project deployment

---

## 👤 Author

**Anand Ramesh**

---

## 📌 Keywords

Retail Analytics | Demand Forecasting | Inventory Optimization | Data Science | Machine Learning | Time Series | Python | Streamlit

