import pygal
import chart

def render(chart_data):
    rows = chart_data['rows']

    config = chart.gu_config()
    config.print_values = False

    radar = pygal.Radar(style=chart.gu_style(rows), config=config)
    radar.x_labels = chart_data['x_labels']
    radar.y_labels = chart_data.get('y_labels')
    for row in rows:
        radar.add(row['label'], row['value'])
    return radar
