import pandas as pd


def insert_csv(file_path: str):
    pass
db = r"C:/Users/raf88/Desktop/Historia_Operacji_2023-08-13_11-02-01.csv"
df = pd.read_csv(db, encoding="windows-1250", sep=";", header=1)
fixed_db = df.to_csv('fixed_data.csv',  index=False) # this step deletes the extra comma that pandas put before the first column name
ok_df = pd.read_csv('fixed_data.csv')
print(ok_df)
