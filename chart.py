#!/usr/bin/python
import sys, json

chart_data = json.loads(sys.stdin.read())
module = __import__('handlers.%s' % chart_data['type'], fromlist=['render'])

chart = module.render(chart_data)
chart.title = chart_data['title']
print chart.render()
