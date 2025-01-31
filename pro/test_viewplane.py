#!/usr/bin/python3

def check_hitpoint(comment, given, expected):
    fail = False
    print(comment)
    if given[0] != expected[0]:
        print(' -- Success Values Different')
        fail = True
    if abs(given[1] - expected[1]) > 0.01:
        print(' -- t values are Different')
        fail = True
    if abs(given[2].v[0] - expected[2].v[0]) > 0.001 or abs(given[2].v[1] - expected[2].v[1]) > 0.001 or abs(given[2].v[2] - expected[2].v[2]) > 0.001:
        print(' -- Hit Point is Different')
        fail = True
    if abs(given[3].v[0] - expected[3].v[0]) > 0.001 or abs(given[3].v[1] - expected[3].v[1]) > 0.001 or abs(given[3].v[2] - expected[3].v[2]) > 0.001:
         print(' -- Color is Different')
         fail = True
    if not fail:
        print(' -- Test Case Passed')
    else:
        print(' -- Expected: '+str(expected))
        print(' -- Received: '+str(given))
        print(' FF Test Case FAILED')

def check_point(comment, given, expected):
    fail = False
    print(comment)
    if abs(given.v[0] - expected.v[0]) > 0.001 or abs(given.v[1] - expected.v[1]) > 0.001 or abs(given.v[2] - expected.v[2]) > 0.001:
        print(' -- Point is Different')
        fail = True
    if not fail:
        print(' -- Test Case Passed')
    else:
        print(' -- Expected: '+str(expected))
        print(' -- Received: '+str(given))
        print(' FF Test Case FAILED')

from graphics import *

p = ViewPlane(Point3D(0,0,0), Normal(1,1,-1), 640, 480, 1).get_point(250, 100)
check_point('Part2 - Test 1 - ViewPlane(Point3D(0,0,0), Normal(1,1,-1), 640, 480, 1).get_point(250, 100)', p, Point3D(147.78531727, 14.8492424, 162.63455967))
p = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1).get_point(250, 100)
check_point('Part2 - Test 2 - ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1).get_point(250, 100)', p, Point3D(-219.5, 10.5, 0))
p = ViewPlane(Point3D(7,9,12.2), Normal(0.2,0.7,0.83), 640, 480, 1).get_point(250, 100)
check_point('Part2 - Test 3 - ViewPlane(Point3D(7,9,12.2), Normal(0.2,0.7,0.83), 640, 480, 1).get_point(250, 100)', p, Point3D(-208.11405221, 17.96444226, 56.47433839))
