import pandas as pd

PLAYERS = {
    8: 'Lamar Jackson',
    89: 'Mark Andrews',
    7: 'Rashod Bateman',
    80: 'Isiah Likely',
    3: 'Odell Beckham Jr.',
    35: 'Gus Edwards',
    15: "Nelson Agholor",
    13: 'Devin Duvernay',
    4: 'Zay Flowers',
    43: 'Justice Hill',
    9: 'Justin Tucker',
    -1: 'Unknown'
}


def is_valid_yd_line(yd_line: int):
    return yd_line >= 0 and yd_line <= 100


def get_avg_yds(df: pd.DataFrame):
    return int(df.sum() / len(df))

