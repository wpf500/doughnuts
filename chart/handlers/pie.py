from itertools import cycle, izip
import pygal

def render(chart, style, inner_radius=0):
    rows = chart['rows']

    style.colors = [row.get('colour', alt) for row, alt in
            izip(rows, cycle(style.colors))]

    pie = pygal.Pie(style=style, js=[],
            inner_radius=inner_radius,
            value_font_size=14,
            font_family='arial')
    for row in rows:
        pie.add(row['label'], row['value'])
    return pie
