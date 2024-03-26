import pandas as pd 

df = pd.read_csv(r'resources/departments.csv', sep = ';')
#print(df.iloc[1])
#print(df.head())
for _, row in df.iterrows():
    values = list(row)
    print(tuple(row))