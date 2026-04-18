from src.generate_data import generate_sales_data
from src.data_preprocessing import load_data, preprocess_data
from src.forecasting import forecast_per_product
from src.inventory import calculate_inventory
from src.evaluation import calculate_metrics
from src.visualization import plot_forecast, plot_residuals
import os

os.makedirs("outputs/plots", exist_ok=True)

# Generate data
generate_sales_data()

# Load + preprocess
df = load_data("data/raw_sales.csv")
df = preprocess_data(df)

# Forecast
df = forecast_per_product(df)

# Inventory
inventory = calculate_inventory(df)

# Evaluation
metrics = calculate_metrics(df)

# Save
df.to_csv("outputs/forecasts.csv", index=False)
inventory.to_csv("outputs/inventory_plan.csv", index=False)
metrics.to_csv("outputs/metrics.csv", index=False)

# Plots
plot_forecast(df)
plot_residuals(df)

print("✅ Advanced project with evaluation completed!")