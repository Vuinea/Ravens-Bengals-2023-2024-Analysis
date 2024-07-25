from utils import team_stats, player_stats, utils
from utils.data import df


# redzone_tds = team_stats.get_redzone_tds(df)
ans = player_stats.get_best_redzone_target_by_yards(df)

# print(ans[['Play Type', 'Run']])
# print(ans.columns)

# print(type(ans))
# print(ans['YD Line'])

print(ans['YDs Gained'])

