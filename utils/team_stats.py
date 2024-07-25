import pandas as pd

def get_run_plays(df: pd.DataFrame):
    return df[df['Run'] == True]

def get_pass_plays(df: pd.DataFrame):
    return df[df['Run'] == False]

def get_plays_from_down(df: pd.DataFrame, down: int):
    return df[df['Down'] == down]

def get_touchdowns(df: pd.DataFrame):
    return df[df['TD'] == True]

def get_redzone_tds(df: pd.DataFrame):
    tds = get_touchdowns(df)
    return tds[tds['YD Line'] >= 80]
    
# whenever a first down or td was reached
def get_conversions(df: pd.DataFrame, tds=False):
    first_downs = df[df['First Down Conversion'] == True]
    if tds:
        tds = get_touchdowns(df)
        return pd.concat(first_downs, tds)
    return first_downs
