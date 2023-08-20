import pandas as pd
# TODO For future division of functionalities of analyser.py

def insert_csv(file_path: str):
    db = file_path
    df = pd.read_csv(db, encoding='windows-1250', sep=";", header=1,
                     index_col=False)

    for i in range(len(df)):
        yield (df['Szczegóły transakcji'][i], df['Kwota operacji'][i], df['Data transakcji'][i])








