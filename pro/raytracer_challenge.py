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

#3 Camera positions 
Camera1 = Ray(Point3D(0,0,-100), Normal(0,0,1))
Camera2 = Ray(Point3D(0,0,-1000), Normal(0,0,1))
Camera3 = Ray(Point3D(-100,-100,-30), Normal(0,0,1))

#4 example viewplanes. 
vp1 = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1.0)
x = Raytracer(vp1, obs)
x.pRaytrace(vp1, obs, Camera1)
PPM(vp1, 'vp1_challenge.ppm')

x.pRaytrace(vp1, obs, Camera2)
PPM(vp1, 'vp2_challenge.ppm')

x.pRaytrace(vp1, obs, Camera3)
PPM(vp1, 'vp3_challenge.ppm')