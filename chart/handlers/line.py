import pygal
import chart

def render(chart_data, type_=pygal.Line):
    rows = chart_data['rows']

    config = chart.gu_config()
    config.css.append('style/line.css')
    config.height = 450
    config.show_dots = type_ == pygal.Line
    config.print_values = False

    line = type_(style=chart.gu_style(rows), config=config)
    line.x_labels = chart_data['x_labels']
    line.y_title = chart_data.get('y_label')
    line.y_labels = chart_data.get('y_labels')
    for row in rows:
        line.add(row['label'], row['value'])
    return line
