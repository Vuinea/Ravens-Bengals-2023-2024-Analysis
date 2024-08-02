from ravens.ravens import player_stats, team_stats
from bokeh.plotting import show
from ravens.graph import graph_plays

# redzone_tds = team_stats.get_redzone_tds(df)
ans = team_stats.get_team_flags(False)
# player = utils.PLAYERS[ans.iloc[0]['Target']]
# print(ans[['Play Type', 'Run']])
# print(ans.columns)

# print(type(ans))
# print(ans['YD Line'])

# print(ans[["Target", 'YDs Gained', 'Play Type', 'Flag', 'Offense']])
# print(ans[['Target Name', 'YDs Left', 'YD Line']])
# print(ans.iloc[0]['Target Name'])
# print(player)

# show the results
p = graph_plays()
show(p)
