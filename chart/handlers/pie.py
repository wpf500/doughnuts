import pygal, webcolors, colorsys

import chart

def text_color(css_color, light, dark):
    if css_color[0] == '#':
        color = webcolors.hex_to_rgb(css_color)
    else:
        color = webcolors.name_to_rgb(css_color)
    color = colorsys.rgb_to_hls(*(a / 255. for a in color))
    return light if color[1] < 0.7 else dark

def render(chart_data, inner_radius=0):
    rows = chart_data['rows']

    total = sum(row['value'] for row in rows) * 1.

    style = chart.gu_style(rows)
    style.text_colors = [
        text_color(color, 'white' if row['value'] / total > 0.04 else style.foreground_light, style.foreground_light)
            for row, color in zip(rows, style.colors)
    ]

    config = chart.gu_config()
    config.inline_legend = True

    # for doughnuts
    config.inner_radius = inner_radius
    config.inner_label = chart_data.get('inner_label')

    pie = pygal.Pie(style=style, config=config)
    for row in rows:
        pie.add(row['label'], row['value'])
    return pie
