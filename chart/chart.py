#!/usr/bin/python
from pygal.style import Style

# create a new Style each time because we can overwrite colours
def style():
    return Style(
        background='white',
        plot_background='white',
        foreground='rgba(0, 0, 0, 0.7)',
        foreground_light='rgba(0, 0, 0, 0.9)',
        foreground_dark='rgba(0, 0, 0, 0.5)',
        colors=('#242424', '#9f6767', '#92ac68',
                '#d0d293', '#9aacc3', '#bb77a4',
                '#77bbb5', '#777777'))

def render(chart_data):
    module = __import__('handlers.%s' % chart_data['type'], fromlist=['render'])

    chart = module.render(chart_data, style())

    chart.title = chart_data['title']
    chart.add_source(chart_data.get('source'))

    return chart.render()
