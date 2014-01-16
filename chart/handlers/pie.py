import pygal
from pygal.style import LightStyle

def render(chart):
    style = LightStyle
    style.colors = tuple(row['colour'] for row in chart['rows'])
    style.plot_background = style.background
    pie = pygal.Pie(style=LightStyle)
    for row in chart['rows']:
        pie.add(row['label'], row['value'])
    return pie
