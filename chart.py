#!/usr/bin/python
import sys, json

chart_data = json.loads(sys.stdin.read())

module = __import__('handlers.%s' % chart_data['type'], fromlist=['render'])

print '<html>'
print '<head><link rel="stylesheet" href="style.css" /></head>'
print '<body><svg xmlns="http://www.w3.org/2000/svg">'

module.render(chart_data)

print '</svg></body></html>'
