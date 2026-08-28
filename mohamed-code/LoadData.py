import pandas as pd

def load_data():
    df = pd.read_csv('Dataset/framingham.csv')
    df = clean_data(df)
    return df

def clean_data(df):
    
    df = df.duplicates_drop()
    
    return df

df = load_data()

print(df.describe())