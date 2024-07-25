import pandas as pd

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
        results = pd.concat(results, tds)
    return results

def get_flags(df: pd.DataFrame) -> pd.DataFrame:
    pass


def get_team_flags(df: pd.DataFrame, offense: bool) -> pd.DataFrame:
    pass
