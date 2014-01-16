import math

radius = 100
text_radius = 120
d_radius = 40

def polar2cart(r, angle):
    return [r * -math.sin(angle), r * math.cos(angle)]

def render(chart_data):
    data = chart_data['data']

    print '<g transform="translate(%d, %d)">' % (radius, radius)

    total = sum(float(row['value']) for row in data)
    angles = [2 * math.pi * float(row['value']) / total for row in data]

    arc_x1 = 0
    arc_y1 = radius
    arc_angle = 2 * math.pi

    outlines = ''

    for angle, row in zip(angles, data):
        text_angle = arc_angle - angle / 2
        text_x, text_y = polar2cart(text_radius, text_angle)
        print '<text class="doughnut-label" x="%f" y="%f">%s</text>' % (text_x, text_y, row['label'])

        arc_angle -= angle;
        arc_x2, arc_y2 = polar2cart(radius, arc_angle)
        arc_cw = 1 if angle > math.pi else 0
        print '<path class="doughnut-arc" fill="%s" d="M 0 0 L %f %f A %d %d 0 %d 0 %f %f" />' % (row['color'], arc_x1, arc_y1, radius, radius, arc_cw, arc_x2, arc_y2)

        arc_x1 = arc_x2
        arc_y1 = arc_y2

    print '<circle cx="0" cy="0" r="%d" fill="white" />' % d_radius
    print '<text class="doughnut-label" x="0" y="0" alignment-baseline="middle" text-anchor="middle">%s</text>' % chart_data['label_middle']
    print '</g>'
