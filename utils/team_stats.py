import pandas as pd
from .utils import Utils

class TeamStats:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_run_plays(self) -> pd.DataFrame:
        return self.df[self.df['Run'] == True]

    def get_pass_plays(self) -> pd.DataFrame:
        return self.df[self.df['Run'] == False]

    def get_plays_from_down(self, down: int) -> pd.DataFrame:
        return self.df[self.df['Down'] == down]

    def get_touchdowns(self) -> pd.DataFrame:
        return self.df[self.df['TD'] == True]

    def get_redzone_tds(self) -> pd.DataFrame:
        tds = self.get_touchdowns()
        return tds[tds['YD Line'] >= 80]
        
    # whenever a first down or td was reached
    def get_conversions(self, tds=False) -> pd.DataFrame:
        results = self.df[self.df['First Down Conversion'] == True]
        if tds:
            tds = self.get_touchdowns()
            results = pd.concat([results, tds])
        return results

    def get_flags(self) -> pd.DataFrame:
        pass


    def get_team_flags(self, offensive: bool) -> pd.DataFrame:
        pass


    def get_all_avg_yards(self) -> pd.DataFrame:
        groups = self.df.groupby('Play Type')
        avg_yds = groups['YDs Gained'].apply(Utils.get_avg_yds)
        return avg_yds

    # gets the play with the most yards per attempt
    def get_most_efficient_play(self) -> pd.DataFrame:
        avg_yds = self.get_all_avg_yards()
        most_efficient_play = avg_yds.idxmax()
        return self.df[self.df['Play Type'] == most_efficient_play]



    # who has the most conversions from a certain yard line to another, if -1 then it will just get it from all of the yard linese
    # Returns all of the targets by the player
    def get_best_third_down_target(self, yd_line_start: int=-1,  yd_line_end: int=-1, tds=False) -> pd.DataFrame:
        # getting all the third down conversions
        conversions = self.get_conversions(tds=tds)
        conversions = conversions[conversions['Down'] == 3]

        # best target in a certain range of yard lines
        if Utils.is_valid_yd_line(yd_line_start) and Utils.is_valid_yd_line(yd_line_end):
            conversions = conversions[(conversions['YD Line'] >= yd_line_start) & (conversions['YD Line'] <= yd_line_end)]

        players = conversions['Target']
        # getting the player with the most amount of succesful targets
        most_conversions = players.value_counts().idxmax()

        return conversions[conversions['Target'] == most_conversions]
        

    # getting the target with the most yards in the red zone
    # Returns all of the plays made by the player
    def get_best_redzone_target_by_yards(self) -> pd.DataFrame:
        redzone_completions = self.df[(self.df['YD Line'] >= 80) & (self.df['Completion'] != 0)]
        yds_gained = redzone_completions.groupby(['Target']).sum(True)['YDs Gained']
        best_redzone_player = yds_gained.idxmax()

        return redzone_completions[redzone_completions['Target'] == best_redzone_player]

    # getting the target with the most tds and first downs in the red zone
    # Returns all of the conversions made by the player
    def get_best_redzone_target_by_conversions(self) -> pd.DataFrame:
        conversions = self.get_conversions(tds=True)
        red_zone_conversions = conversions[conversions['YD Line'] >= 80]
        grouped_conversions = red_zone_conversions.groupby(['Target'])
        player = grouped_conversions.size().idxmax()
        return red_zone_conversions[red_zone_conversions['Target'] == player]
        
    # value counts
    # .apply()

    # getting the target with the best completion percentage
    def get_best_redzone_target_by_completion_percentage(self) -> pd.DataFrame:
        redzone_passes = self.df[self.df['YD Line'] >= 80]
        # getting rid of all the rows with -1 as target
        redzone_passes = redzone_passes.loc[self.df['Target'] >= 0]
        grouped_passes = redzone_passes.groupby('Target', sort=False)

        passes = grouped_passes.apply(Utils.get_completion_percentage)
        passes = passes.astype(int)
        player = passes.idxmax()
        return redzone_passes[redzone_passes['Target'] == player]

    def _get_conversion_percentage(self):
        conversions = len(self.df[self.df['First Down Conversion'] == True])
        return conversions / len(self.df)

    # name subject to change
    def get_best_third_down_by_yds_left(self, yds_left: int, specificity: str) -> pd.DataFrame:
        specificity = specificity.lower().strip()
        if specificity == 'greater':
            plays = self.df[(self.df['YDs Left'] >= yds_left) & (self.df['Down'] == 3)]
        elif specificity == 'less':
            plays = self.df[(self.df['YDs Left'] <= yds_left) & (self.df['Down'] == 3)]
        else:
            plays = self.df[(self.df['YDs Left'] == yds_left) & (self.df['Down'] == 3)]

        # getting player with most conversions by percentage
        grouped_plays = plays.groupby('Target', sort=False)
        
        conversion_percentages = grouped_plays.apply(self.get_conversion_percentage)
        if len(conversion_percentages) != 0:
            best_player = conversion_percentages.idxmax()
            return plays[plays['Target'] == best_player]
        else:
            return pd.DataFrame()

    # get player with the most first downs
    def get_best_converter(self) -> pd.DataFrame:
        first_downs = self.df[self.df['First Down Conversion'] == True]
        player = first_downs['Target'].mode()
        values = player.values
        return first_downs[first_downs['Target'].isin(values)]


    # gets the player with the most yards based on the quarter
    def get_best_player_yardage(self, quarter: int) -> pd.DataFrame:
        if quarter < 0:
            plays = self.df
        else:
            plays = self.df[self.df['Quarter'] == quarter]
        groups = plays.groupby('Target')
        avg_yds = groups['YDs Gained'].apply(Utils.get_avg_yds)
        player = avg_yds.idxmax()
        return plays[plays['Target'] == player]

