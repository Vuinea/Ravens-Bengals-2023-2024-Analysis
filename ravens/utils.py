import pandas as pd
import numpy as np

# dictionary of player names
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

class Utils:
    def __init__(self):
        pass
    
    @staticmethod
    def is_valid_yd_line(yd_line: int):
        return yd_line >= 0 and yd_line <= 100


    @staticmethod
    def get_avg_yds(df: pd.DataFrame):
        return int(df.sum() / len(df))

    @staticmethod
    def get_completion_percentage(plays: pd.DataFrame, player: np.int64):
        plays = plays[plays['Target'] == player]
        attempts = plays['Completion'].value_counts()
        if 1 in attempts.index:
            completions = attempts[1]
            if 0 in attempts.index:
                passing_attempts = attempts[1] + attempts[0]
            else:
                passing_attempts = completions
        else:
            completions = 0
            # setting default value for passing attemots
            passing_attempts = 1
        return (completions/passing_attempts) * 100

    @staticmethod
    def get_completion_percentage(df: pd.DataFrame):
        attempts = df['Completion'].value_counts()
        if 1 in attempts.index:
            completions = attempts[1]
            if 0 in attempts.index:
                passing_attempts = attempts[1] + attempts[0]
            else:
                passing_attempts = completions
        else:
            completions = 0
            # setting default value for passing attemots
            passing_attempts = 1
        return (completions/passing_attempts) * 100
