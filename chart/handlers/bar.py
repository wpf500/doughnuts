import pygal
import chart

def render(chart_data):
    rows = chart_data['rows']

    config = chart.gu_config()
    config.height = 450
    config.print_values = False
    config.css.append('style/bar.css')

    bar = pygal.Bar(style=chart.gu_style(rows), config=config)
    bar.x_labels = chart_data['x_labels']
    bar.y_labels = chart_data.get('y_labels')
    for row in rows:
        bar.add(row['label'], row['value'])
    return bar
