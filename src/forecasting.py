from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

def forecast_per_product(df):
    result = []

    for product in df['product'].unique():
        temp = df[df['product'] == product].copy()

        # Sort
        temp = temp.sort_values('date')

        # Set index
        temp.set_index('date', inplace=True)

        # Ensure daily frequency
        temp = temp.asfreq('D')

        # Fill missing values
        temp['sales'] = temp['sales'].ffill()

        # ARIMA model
        model = ARIMA(temp['sales'], order=(2,1,2))
        model_fit = model.fit()

        # In-sample forecast
        temp['forecast'] = model_fit.predict(start=0, end=len(temp)-1)

        # Future forecast (7 days)
        future_forecast = model_fit.forecast(steps=7)

        future_dates = pd.date_range(
            start=temp.index[-1] + pd.Timedelta(days=1),
            periods=7
        )

        future_df = pd.DataFrame({
            "date": future_dates,
            "product": product,
            "category": temp['category'].iloc[0],
            "sales": None,
            "forecast": future_forecast.values
        })

        temp = temp.reset_index()

        result.append(temp)
        result.append(future_df)

    return pd.concat(result, ignore_index=True)