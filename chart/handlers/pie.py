import pygal
from pygal.style import LightStyle

def render(chart):
    pie = pygal.Pie(style=LightStyle)
    for row in chart['data']:
        pie.add(row['label'], row['value'])
    return pie
