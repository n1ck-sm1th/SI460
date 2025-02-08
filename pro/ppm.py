import graphics as g
from graphics import *

class PPM:
    def __init__(self, ViewPlaneObject, filename, *args):
        self.ViewPlaneObject = ViewPlaneObject
        self.filename = filename   
        self.hres, self.vres = self.ViewPlaneObject.get_resolution()
        
        with open(filename, "w") as f: #GenAI 2
            f.write("P3\n")  # PPM magic number
            f.write(f"{self.hres} {self.vres}\n")  # Image dimensions
            f.write(f"{255}\n")  # Maximum color value
            
            for y in reversed(range(self.vres)):
                for x in range(self.hres):
                    red, green, blue = self.ViewPlaneObject.get_color(y, x).get()
                    f.write(f"{int(red*255)} {int(green*255)} {int(blue*255)} ")  # RGB values (red, green, blue)
                f.write("\n")

myViewPlane = ViewPlane(Point3D(0,0,0), g.Normal(0,0,1), 3, 4, 1)
myViewPlane.set_color(0,0,ColorRGB(1,1,1))
myViewPlane.set_color(0,2,ColorRGB(1,0,0))
myViewPlane.set_color(1,1,ColorRGB(1,0,1))
myViewPlane.set_color(1,2,ColorRGB(1,1,0))
myViewPlane.set_color(3,0,ColorRGB(0,1,0))
myViewPlane.set_color(3,2,ColorRGB(0,0,1))

PPM(myViewPlane, 'part3-testing.ppm')