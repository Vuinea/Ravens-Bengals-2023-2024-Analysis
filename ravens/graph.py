from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, LabelSet
from .ravens import team_stats, player_stats



def graph_plays():
    counted_plays = team_stats.count_plays(include_special=False)

    x = counted_plays.keys().to_list()
    y = counted_plays.values.tolist()

    source = ColumnDataSource(dict(x=x, y=y))

    p = figure(title="Plays per Play Type", x_range=x, y_axis_label="Times Executed")

    p.vbar(x=x, top=y, width=0.5, color='#241773')

    return p
