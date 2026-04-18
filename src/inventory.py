import numpy as np
import pandas as pd

def calculate_inventory(df):
    lead_time = 5
    service_level = 1.65

    results = []

    for product in df['product'].unique():
        temp = df[df['product'] == product]

        std_dev = np.std(temp['forecast'])

        safety_stock = service_level * std_dev * np.sqrt(lead_time)
        reorder_point = temp['forecast'].mean() * lead_time + safety_stock

        results.append({
            "product": product,
            "avg_forecast": temp['forecast'].mean(),
            "safety_stock": safety_stock,
            "reorder_point": reorder_point
        })

    return pd.DataFrame(results)