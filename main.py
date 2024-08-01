from utils import team_stats, player_stats, utils
from utils.data import df


# redzone_tds = team_stats.get_redzone_tds(df)
ans = player_stats.get_best_player_yardage(df, 4)
# player = utils.PLAYERS[ans.iloc[0]['Target']]
# print(ans[['Play Type', 'Run']])
# print(ans.columns)

# print(type(ans))
# print(ans['YD Line'])

print(ans[["Target", 'YDs Gained']])
# print(ans[['Target Name', 'YDs Left', 'YD Line']])
# print(ans.iloc[0]['Target Name'])
# print(player)

