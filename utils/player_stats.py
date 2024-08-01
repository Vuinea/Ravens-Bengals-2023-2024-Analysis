import pandas as pd
from . import team_stats, utils



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
# Returns all of the conversions made by the player
def get_best_redzone_target_by_conversions(df: pd.DataFrame) -> pd.DataFrame:
    conversions = team_stats.get_conversions(df, tds=True)
    red_zone_conversions = conversions[conversions['YD Line'] >= 80]
    grouped_conversions = red_zone_conversions.groupby(['Target'])
    player = grouped_conversions.size().idxmax()
    return red_zone_conversions[red_zone_conversions['Target'] == player]
    
# value counts
# .apply()

def _get_completion_percentage(df: pd.DataFrame):
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

# getting the target with the best completion percentage
def get_best_redzone_target_by_completion_percentage(df: pd.DataFrame) -> pd.DataFrame:
    redzone_passes = df[df['YD Line'] >= 80]
    # getting rid of all the rows with -1 as target
    redzone_passes = redzone_passes.loc[df['Target'] >= 0]
    grouped_passes = redzone_passes.groupby('Target', sort=False)

    passes = grouped_passes.apply(_get_completion_percentage)
    passes = passes.astype(int)
    player = passes.idxmax()
    return redzone_passes[redzone_passes['Target'] == player]

def _get_conversion_percentage(df: pd.DataFrame):
    conversions = len(df[df['First Down Conversion'] == True])
    return conversions / len(df)

# name subject to change
def get_best_third_down_by_yds_left(df: pd.DataFrame, yds_left: int, specificity: str) -> pd.DataFrame:
    specificity = specificity.lower().strip()
    if specificity == 'greater':
        plays = df[(df['YDs Left'] >= yds_left) & (df['Down'] == 3)]
    elif specificity == 'less':
        plays = df[(df['YDs Left'] <= yds_left) & (df['Down'] == 3)]
    else:
        plays = df[(df['YDs Left'] == yds_left) & (df['Down'] == 3)]

    # getting player with most conversions by percentage
    grouped_plays = plays.groupby('Target', sort=False)
    
    conversion_percentages = grouped_plays.apply(_get_conversion_percentage)
    if len(conversion_percentages) != 0:
        best_player = conversion_percentages.idxmax()
        print(conversion_percentages)
        return plays[plays['Target'] == best_player]
    else:
        return pd.DataFrame()

# get player with the most first downs
def get_best_converter(df: pd.DataFrame) -> pd.DataFrame:
    first_downs = df[df['First Down Conversion'] == True]
    player = first_downs['Target'].mode()
    values = player.values
    return first_downs[first_downs['Target'].isin(values)]


# gets the player with the most yards based on the quarter
def get_best_player_yardage(df: pd.DataFrame, quarter: int) -> pd.DataFrame:
    if quarter < 0:
        plays = df
    else:
        plays = df[df['Quarter'] == quarter]
    groups = plays.groupby('Target')
    avg_yds = groups['YDs Gained'].apply(utils.get_avg_yds)
    player = avg_yds.idxmax()
    return plays[plays['Target'] == player]
