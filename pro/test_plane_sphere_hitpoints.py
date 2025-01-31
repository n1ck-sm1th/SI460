#!/usr/bin/python3

from graphics import *

def check_hitpoint(comment, expected, given, ignore_success=True):
    fail = False
    results = comment + '\n'
    print(comment)
    if given[0] != expected[0] and ignore_success:
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

hit = Plane(Point3D(1,1,1), Normal(2,3,1)).hit(Ray(Point3D(2,2,-2), Vector3D(0,0,1)), 0.000001)
# (True, -2.0, [ 2.  2. -4.], [ 1.  1.  1.])
check_hitpoint('Test Case 1 - Plane(Point3D(1,1,1), Normal(2,3,1)).hit(Ray(Point3D(2,2,-2), Vector3D(0,0,1)), 0.000001)', (True, -2.0, Point3D(2,2,-4), ColorRGB(1,1,1)), hit, False)

hit = Plane(Point3D(5,6,7), Normal(8,7,2)).hit(Ray(Point3D(1,2,-3), Vector3D(0,2,1)), 0.000001)
check_hitpoint('Test Case 2 - Plane(Point3D(5,6,7), Normal(8,7,2)).hit(Ray(Point3D(1,2,-3), Vector3D(0,2,1)), 0.000001)', (True, 5.0, Point3D(1,12,2), ColorRGB(1,1,1)), hit)

# sphere = Sphere(Point3D(0,0,0), 10.0)
# ray = Ray(Point3D(2,2,-20), Vector3D(0,0,1))
# hit = sphere.hit(ray, 0.000001)
hit = Sphere(Point3D(0,0,0), 10.0).hit(Ray(Point3D(2,2,-20), Vector3D(0,0,1)), 0.000001)
check_hitpoint('Test Case 3 - Sphere(Point3D(0,0,0), 10.0).hit(Ray(Point3D(2,2,-20), Vector3D(0,0,1)), 0.000001)', (True, 10.40833695, Point3D(2,2,-9.591663), ColorRGB(1,1,1)), hit)

hit = Sphere(Point3D(2,3,4), 12.0).hit(Ray(Point3D(3.5,3.5,-20), Vector3D(0.3,0.2,0.9)), 0.000001)
# (True, 16.129429863917917, [ 8.33882896  6.72588597 -5.48351312], [ 1.  1.  1.])
check_hitpoint('Test Case 4 - Sphere(Point3D(2,3,4), 12.0).hit(Ray(Point3D(3.5,3.5,-20), Vector3D(0.3,0.2,0.9)), 0.000001)', (True, 16.1294298, Point3D(8.33882896, 6.72588597, -5.48351312), ColorRGB(1,1,1)), hit)
