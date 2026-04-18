import numpy as np
import pandas as pd

def calculate_metrics(df):
    """
    Calculate MAE, RMSE, and MAPE per product.
    Handles missing values and avoids division errors.
    """

    results = []

    for product in df['product'].unique():
        temp = df[df['product'] == product].copy()

        # Drop rows where actual or forecast is missing
        temp = temp.dropna(subset=['sales', 'forecast'])

        if len(temp) == 0:
            continue

        actual = temp['sales']
        predicted = temp['forecast']

        # Metrics
        mae = np.mean(np.abs(actual - predicted))
        rmse = np.sqrt(np.mean((actual - predicted) ** 2))

        # Avoid division by zero in MAPE
        actual_safe = actual.replace(0, np.nan)
        mape = np.mean(np.abs((actual - predicted) / actual_safe)) * 100

        results.append({
            "product": product,
            "MAE": round(mae, 2),
            "RMSE": round(rmse, 2),
            "MAPE (%)": round(mape, 2)
        })

    return pd.DataFrame(results)