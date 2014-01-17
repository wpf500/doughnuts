import pygal
import line

def render(chart_data):
    def stacked(*args, **kwargs):
        return pygal.StackedLine(*args, fill=True, **kwargs)
    return line.render(chart_data, stacked)
