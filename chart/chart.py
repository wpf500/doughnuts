#!/usr/bin/python
def render(chart_data):
    module = __import__('handlers.%s' % chart_data['type'], fromlist=['render'])

    chart = module.render(chart_data)

    chart.title = chart_data['title']
    chart.add_source(chart_data.get('source'))

    return chart.render()
