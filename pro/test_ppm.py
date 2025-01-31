goal = ['P3', '3 5', '255', '0 0 0', '0 0 0', '0 0 0', '0 255 0', '0 0 0', '0 0 255', '0 0 0', '0 0 0', '0 0 0', '0 0 0', '255 0 255', '255 255 0', '255 255 255', '0 0 0', '255 0 0']
pgoal = []

for row in goal:
    for x in row.split(' '):
        pgoal.append(x)

import graphics as g
from ppm import PPM

myViewPlane = g.ViewPlane(g.Point3D(0,0,0), g.Normal(0,0,1), 3, 5, 1)
myViewPlane.set_color(0,0,g.ColorRGB(1,1,1))
myViewPlane.set_color(0,2,g.ColorRGB(1,0,0))
myViewPlane.set_color(1,1,g.ColorRGB(1,0,1))
myViewPlane.set_color(1,2,g.ColorRGB(1,1,0))
myViewPlane.set_color(3,0,g.ColorRGB(0,1,0))
myViewPlane.set_color(3,2,g.ColorRGB(0,0,1))

PPM(myViewPlane, 'part2-testing-submit.ppm')

with open('part2-testing-submit.ppm') as f:
    tmp = f.readlines()
    results = []
    for line in tmp:
        line = line.strip()
        if line != '':
            results.append(line)
    pcheck = []
    for row in results:
        row = row.replace('\t', ' ')
        row = row.strip()
        for x in row.split(' '):
            if x != ' ' and x != '':
                pcheck.append(x)
    # print(['goal', pgoal])
    # print(['chek', pcheck])
    if pgoal == pcheck or results == ['P3', '3 5', '255', '0 0 0', '0 0 0', '0 0 0', '0 255 0', '0 0 0', '0 0 255', '0 0 0', '0 0 0', '0 0 0', '0 0 0', '255 0 255', '255 255 0', '255 255 255', '0 0 0', '255 0 0']:
        print('PASSED')
    else:
        print('DOES NOT MATCH')
    for line in results:
        print(line)
