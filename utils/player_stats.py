import pandas as pd
from . import team_stats, utils
import numpy as np



# who has the most conversions from a certain yard line to another, if -1 then it will just get it from all of the yard linese
# Returns all of the targets by the player
def get_best_third_down_target(df: pd.DataFrame, yd_line_start: int=-1,  yd_line_end: int=-1, tds=False) -> pd.DataFrame:
    # getting all the third down conversions
    conversions = team_stats.get_conversions(df, tds=tds)
    conversions = conversions[conversions['Down'] == 3]

    # best target in a certain range of yard lines
    if utils.is_valid_yd_line(yd_line_start) and utils.is_valid_yd_line(yd_line_end):
        conversions = conversions[(conversions['YD Line'] >= yd_line_start) & (conversions['YD Line'] <= yd_line_end)]

    players = conversions['Target']
    # getting the player with the most amount of succesful targets
    most_conversions = players.value_counts().idxmax()

    return conversions[conversions['Target'] == most_conversions]
    

# getting the target with the most yards in the red zone
# Returns all of the plays made by the player
def get_best_redzone_target_by_yards(df: pd.DataFrame) -> pd.DataFrame:
    redzone_completions = df[(df['YD Line'] >= 80) & (df['Completion'] != 0)]
    yds_gained = redzone_completions.groupby(['Target']).sum(True)['YDs Gained']
    best_redzone_player = yds_gained.idxmax()

    return redzone_completions[redzone_completions['Target'] == best_redzone_player]

# getting the target with the most tds and first downs in the red zone
def get_best_redzone_target_by_conversions(df: pd.DataFrame) -> np.int64:
    pass

# getting the target with the best completion percentage
def get_best_redzone_target_by_completion_percentage(df: pd.DataFrame) -> np.int64:
    pass


# name subject to change
def get_best_third_down_based_on_yds_left(df: pd.DataFrame, yds_left: int) -> np.int64:
    pass


# get player with the most first downs
def get_best_converter(df: pd.DataFrame) -> np.int64:
    pass


# gets the player with the most yards based on the quarter
def get_best_player_yardage_by_quarter(df: pd.DataFrame, quarter: int) -> pd.DataFrame:
    pass 


