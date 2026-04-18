import matplotlib.pyplot as plt

def plot_forecast(df):
    for product in df['product'].unique():
        temp = df[df['product'] == product].dropna()

        plt.figure()
        plt.plot(temp['date'], temp['sales'], label='Actual')
        plt.plot(temp['date'], temp['forecast'], label='Forecast')

        plt.title(f"{product} - Forecast vs Actual")
        plt.legend()

        plt.savefig(f"outputs/plots/{product}_forecast.png")
        plt.close()


def plot_residuals(df):
    for product in df['product'].unique():
        temp = df[df['product'] == product].dropna()

        residuals = temp['sales'] - temp['forecast']

        plt.figure()
        plt.plot(residuals)
        plt.title(f"{product} - Residuals")

        plt.savefig(f"outputs/plots/{product}_residuals.png")
        plt.close()