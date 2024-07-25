from utils import team_stats, player_stats
from utils.data import df

ans = team_stats.get_touchdowns(df)

redzone_tds = team_stats.get_redzone_tds(df)

# print(ans[['Play Type', 'Run']])
# print(df.columns)

print(redzone_tds)

