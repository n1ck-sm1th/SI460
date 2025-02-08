from numpy import Infinity
from graphics import *
from raytracer_part4 import Raytracer
from ppm import PPM


# Build the Spheres that will be in our world
S1 = Sphere(Point3D(300,200,200), 100, ColorRGB(1.0,0.2,0.4))
S2 = Sphere(Point3D(-200,-100,50), 35, ColorRGB(0.3,0.8,0.2))
S3 = Sphere(Point3D(50,20,100), 25, ColorRGB(0.4,0.1,0.4))
S4 = Sphere(Point3D(300,-200,600), 250, ColorRGB(0.6,0.6,0.4))
S5 = Sphere(Point3D(400,400,900), 400, ColorRGB(0.0,0.2,1.0))

# Build the Planes that will be in our world
P1 = Plane(Point3D(50,50,999), Normal(0,0,1), ColorRGB(0.8,0.8,0.8))
P2 = Plane(Point3D(50,50,900), Normal(1,1,1), ColorRGB(1.0,1.0,1.0))

# It would make sense to put all of your objects into an array
# so that you can iterate through them.  Here is our observable world:
obs = [S1,S2,S3,S4,S5,P1,P2]

#4 example viewplanes. 
vp1 = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 200, 100, 1.0)
x = Raytracer(vp1, obs)
x.raytrace(vp1, obs)
PPM(vp1, 'vp1.ppm')
vp2 = ViewPlane(Point3D(50,50,-50), Normal(0,0,1), 200, 100, 1.0)
x = Raytracer(vp2, obs)
x.raytrace(vp2, obs)
PPM(vp2, 'vp2.ppm')
vp3 = ViewPlane(Point3D(50,50,-50), Normal(1,1,1), 200, 100, 1.0)
x = Raytracer(vp3, obs)
x.raytrace(vp3, obs)
PPM(vp3, 'vp3.ppm')
vp4 = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1.0)
x = Raytracer(vp4, obs)
x.raytrace(vp4, obs)
PPM(vp4, 'vp4.ppm')
vp5 = ViewPlane(Point3D(50,50,-50), Normal(-0.2,0,1), 200, 100, 1.0)
x = Raytracer(vp5, obs)
x.raytrace(vp5, obs)
PPM(vp5, 'vp5.ppm')




