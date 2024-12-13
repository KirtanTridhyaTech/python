import pandas as pd

df = pd.read_csv('sales.csv', encoding='latin1')

print(df.to_string()) 