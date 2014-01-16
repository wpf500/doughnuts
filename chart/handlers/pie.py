from itertools import cycle, izip
import pygal

import chart

def render(chart_data, inner_radius=0):
    rows = chart_data['rows']

    style = chart.gu_style()
    style.colors = [row.get('colour', alt) for row, alt in
            izip(rows, cycle(style.colors))]

    # for doughnuts
    config = chart.gu_config()
    config.inner_radius = inner_radius
    config.inner_label = chart_data.get('inner_label')

    pie = pygal.Pie(style=style, config=config)
    for row in rows:
        pie.add(row['label'], row['value'])
    return pie
