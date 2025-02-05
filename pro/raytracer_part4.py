from numpy import Infinity
from graphics import *

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

#Gen AI #3
for y in range(height):
    for x in range(width):
        oRay = vp.orthographic_ray(y, x)
        
        closest_object = None
        closest_t = float('inf')
        closest_color = None  
        closest_intersection = None
        
        for object in obs:
            intersection_info = object.hit(oRay, 10**-6)

            if intersection_info is not None:  # Check if there was an intersection
                t = intersection_info[1]

                if t > 0 and t < closest_t:  # Check for positive t and closer intersection
                    closest_t = t
                    closest_object = object
                    closest_intersection = intersection_info[2]
                    closest_color = intersection_info[3]  # Get the object's color at the intersection point

        if closest_object is not None:  # If we hit something
            vp.set_color(y, x, closest_color)  # Set the pixel color on the view plane
            
PPM(vp, 'raytracer.ppm')