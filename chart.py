#!/usr/bin/python
import sys, json

chart_data = json.loads(sys.stdin.read())

module = __import__('handlers.%s' % chart_data['type'], fromlist=['render'])

print '<svg xmlns="http://www.w3.org/2000/svg">'
print '<g transform="translate(400, 300)">'

module.render(chart_data)

print '</g>'
print '</svg>'
