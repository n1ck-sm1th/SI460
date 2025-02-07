#Nick Smith
#265904

from numpy import Infinity
from graphics import *

class Raytracer:
    def __init__(self, vp, obs):
        self

    def raytrace(self, vp, obs):
        for y in range(vp.vres):
            for x in range(vp.hres):
                oRay = vp.orthographic_ray(y, x)
        
                closest_t = float('inf') 
             
                for object in obs: #Check each object.
                    pointFound, t, point, color = object.hit(oRay, 10**-6)
                    
                    if pointFound:  # Check if there was an intersection
                        if t > 10**-6 and t < closest_t:  # Check for positive t and closer intersection
                            closest_t = t
                            vp.set_color(y,x,color)  # Get the object's color at the intersection point
     

    def pRaytrace(self, vp, obs, ray):
            for y in range(vp.vres):
                for x in range(vp.hres):
                    oRay = vp.perspective_ray(y, x, ray.origin)
        
                closest_t = float('inf') 
              
                for object in obs: #Check each object.
                    pointFound, t, point, color = object.hit(oRay, 10**-6)
                    
                    if pointFound:  # Check if there was an intersection
                        if t > 10**-6 and t < closest_t:  # Check for positive t and closer intersection
                            closest_t = t
                            vp.set_color(y,x,color)  # Get the object's color at the intersection point   

if __name__ == '__main__':
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
    
    center = Point3D(0,0,0)
    normal = Normal(0,0,1)
    width = 640
    height = 480
    scalingFactor = 1.0
    vp = ViewPlane(center, normal, width, height, scalingFactor)
    PPM(vp, 'new.ppm')
