#!/usr/bin/python
from pygal.style import Style
from pygal.config import Config

# create a new Style each time because we can overwrite colours
def gu_style():
    return Style(
        opacity=0.7,
        opacity_hover=1,
        background='white',
        plot_background='white',
        foreground='rgba(0, 0, 0, 0.7)',
        foreground_light='rgba(0, 0, 0, 0.9)',
        foreground_dark='rgba(0, 0, 0, 0.5)',
        colors=('#242424', '#9f6767', '#92ac68',
                '#d0d293', '#9aacc3', '#bb77a4',
                '#77bbb5', '#777777'))

# same as above
def gu_config():
    ret = Config(
        js=[],
        value_font_size=18,
        font_family='arial')
    ret.css.append('custom.css')
    return ret

def render(chart_data):
    module = __import__('handlers.%s' % chart_data['type'], fromlist=['render'])

    chart = module.render(chart_data)
    chart.title = chart_data.get('title')
    chart.source = chart_data.get('source')

    return chart.render()
