import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    return df