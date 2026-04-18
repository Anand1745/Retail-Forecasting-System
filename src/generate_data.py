import pandas as pd
import numpy as np

def generate_sales_data():
    np.random.seed(42)

    products = ["Milk", "Bread", "Rice"]
    categories = ["Dairy", "Bakery", "Grocery"]

    dates = pd.date_range(start="2023-01-01", periods=200)

    data = []

    for product, category in zip(products, categories):
        for i, date in enumerate(dates):
            base = 100 + 30*np.sin(i/10)
            noise = np.random.randint(-15, 15)
            sales = base + noise + (20 if product == "Rice" else 0)

            data.append([date, product, category, sales])

    df = pd.DataFrame(data, columns=["date", "product", "category", "sales"])
    df.to_csv("data/raw_sales.csv", index=False)