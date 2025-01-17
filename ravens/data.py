import pandas as pd
import numpy as np
from .utils import PLAYERS

data = pd.read_csv('data.csv')

df = data.copy(deep=True)

def clean_play_types(p: str):
    return p.lower()

def clean_yd_line(yd_line: str):
    if 'b' in yd_line.lower():
        yd_line = 100 - int(yd_line[:-1])
    else:
        yd_line = int(yd_line[:-1])
    return yd_line
    
# altering already existing columns
df['Play Type'] = df['Play Type'].apply(clean_play_types).astype("string")
df['YD Line'] = df['YD Line'].apply(clean_yd_line).astype(int)
df['Down'] = df['Down'].astype(int)
df["TD"] = df['TD'].astype(bool)
df['Quarter'] = df['Quarter'].astype(int)
df['Flag'] = df['Flag'].astype(bool)

# creating new columns

def get_player_name(row: pd.Series):
    return PLAYERS[row['Target']]

df['Run'] = np.where(df['Play Type'].str.contains('run|jet sweep', regex=True), True, False)
df['Special'] = np.where(df['Play Type'].str.contains('fg|punt', regex=True), True, False)
df['First Down Conversion'] = np.where(df['YDs Gained'] >= df['YDs Left'], True, False)
df['Target Name'] = df.apply(get_player_name, axis=1)
