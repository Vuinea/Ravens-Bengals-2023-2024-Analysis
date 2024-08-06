from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models import TapTool
import math
from .ravens import team_stats, player_stats

colors = [
    '#edae49',
    '#d1495b',
    '#00798c',
    '#30638e'
]

curdoc().theme = 'dark_minimal'
# curdoc().theme = 'night_sky'

def graph_plays():
    counted_plays = team_stats.count_plays().sort_index()

    x = counted_plays.keys().to_list()
    x = [i.capitalize() for i in x]
    y = counted_plays.values.tolist()

    quarters = ['Q1', 'Q2', 'Q3', 'Q4']

    data = {
        'play_types': x,
    }
    
    for q in range(1, 5):
        data[f'Q{q}'] = team_stats.count_plays_by_quarter(q, True)


    p = figure(title="Plays per Play Type", x_range=x, y_axis_label="Times Executed", toolbar_location=None, tools='hover', tooltips="$name @play_types: @$name")

    # p.vbar(x=x, top=y, width=0.5, color='#241773')
    p.xaxis.major_label_orientation = math.pi / 4

    p.vbar_stack(quarters, x='play_types', width=0.9, color=colors, source=data,
             legend_label=quarters)
    p.legend.click_policy = 'hide'

    return p
