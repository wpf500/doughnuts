import math

radius = 100

def render(chart_data):
    data = chart_data['data']

    total = sum(float(row['value']) for row in data)
    angles = [2 * math.pi * float(row['value']) / total for row in data]

    x1 = 0
    y1 = radius

    angle_left = 2 * math.pi

    for angle, row in zip(angles, data):
        angle_left -= angle;

        x2 = radius * -math.sin(angle_left)
        y2 = radius * math.cos(angle_left)
        a = 1 if angle > math.pi else 0

        print '<path fill="%s" d="M 0 0 L %f %f A %d %d 0 %d 0 %f %f" />' % (row['color'], x1, y1, radius, radius, a, x2, y2)

        x1 = x2
        y1 = y2
