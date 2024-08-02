import pandas as pd
from . import utils

def get_run_plays(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Run'] == True]

def get_pass_plays(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Run'] == False]

def get_plays_from_down(df: pd.DataFrame, down: int) -> pd.DataFrame:
    return df[df['Down'] == down]

def get_touchdowns(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['TD'] == True]

def get_redzone_tds(df: pd.DataFrame) -> pd.DataFrame:
    tds = get_touchdowns(df)
    return tds[tds['YD Line'] >= 80]
    
# whenever a first down or td was reached
def get_conversions(df: pd.DataFrame, tds=False) -> pd.DataFrame:
    results = df[df['First Down Conversion'] == True]
    if tds:
        tds = get_touchdowns(df)
        results = pd.concat([results, tds])
    return results

def get_flags(df: pd.DataFrame) -> pd.DataFrame:
    pass


def get_team_flags(df: pd.DataFrame, offensive: bool) -> pd.DataFrame:
    pass


def get_all_avg_yards(df: pd.DataFrame) -> pd.DataFrame:
    groups = df.groupby('Play Type')
    avg_yds = groups['YDs Gained'].apply(utils.get_avg_yds)
    return avg_yds

# gets the play with the most yards per attempt
def get_most_efficient_play(df: pd.DataFrame) -> pd.DataFrame:
    avg_yds = get_all_avg_yards(df)
    most_efficient_play = avg_yds.idxmax()
    return df[df['Play Type'] == most_efficient_play]

