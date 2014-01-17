import pygal
import bar

def render(chart_data):
    return bar.render(chart_data, pygal.StackedBar)
