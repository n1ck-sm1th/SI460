#!/usr/bin/python3

# Nick Smith
#265904
import numpy
import math

# Vector 3D class
class Vector3D:
    def __init__(self, val, *args):
        if isinstance(val, numpy.ndarray):
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Vector3D")
    
    def __str__(self):
        '''Represent the string of a vector.'''
        return str(self.v)
    
    def __add__(self, other):
        '''Add two vectors together.'''
        return Vector3D(self.v + other.v)
    
    def __sub__(self, other):
        '''Subtract one vector from another.'''
        if isinstance(other, Vector3D):
            return Vector3D(numpy.subtract(self.v, other.v))
        else: 
            return Vector3D(self.v - other)
        
    def __rsub__(self, other):
        '''Right hand subtraction of a vector'''
        if isinstance(other, Vector3D):
            return Vector3D(numpy.subtract(other.v, self.v))
        else: 
            return Vector3D(other - self.v)
    
    def __mul__(self, other):
        '''Multiply a vector by another vector, overload * operator'''
        if isinstance(other, Vector3D):
            return Vector3D(numpy.dot(self.v, other.v)) #Gen AI #1
        else:
            return Vector3D(self.v * other)
        
    def dot(self, other):
        '''Find the dot product of two vectors'''
        return numpy.dot(self.v, other.v)

    def __truediv__(self, const):
        '''Divide a vector by a constant'''
        return Vector3D(self.v / const)
    
    def magnitude(self):
        '''Find the magnitude of a vector.'''
        return numpy.linalg.norm(self.v)
    
    def copy(self):
        v = Vector3D(self.v)
        return v
    
    def square(self):
        '''Square the magnitude'''
        return (numpy.linalg.norm(self.v))**2
    
    def dotangle(self, other, angle):
        '''Find the dot product using equation 
        |u||v|cos0'''
        return self.magnitude() * other.magnitude() * math.cos(angle)
    
    def cross(self, other):
        '''Cross multipy the vector and another vector.'''
        return Vector3D(numpy.cross(self.v, other.v))
    
#Point3D class
class Point3D:
    def __init__(self, val, *args):
        if isinstance(val, numpy.ndarray):
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Point3D")
    
    def __str__(self):
        return str(self.v)
    
    def __add__(self, other):
        '''Add a point and vector'''
        return Point3D(self.v + other.v)   
    
    def __sub__(self, other):
        '''Subtract one point from another.'''
        if isinstance(other, Point3D):
            return Vector3D(numpy.subtract(self.v, other.v))
        elif isinstance(other, Vector3D): 
            return Point3D(numpy.subtract(self.v, other.v))
    
    def __rsub__(self, other):
        '''Right hand subtraction case of a point'''
        if isinstance(other, Point3D):
            return Vector3D(numpy.subtract(other.v, self.v))
        else: 
            return Point3D(other - self.v)
        
    def __mul__(self, const):
        '''Multiply a point  by a constant'''
        return Point3D(self.v * const)
    
    def distancesquared(self, other):
        '''Find the distance squared between two points'''
        return (numpy.linalg.norm(self.v - other.v))**2 #Gen AI #2 & 3 
    
    def distance(self, other):
        '''Find the distance between two points'''
        return numpy.linalg.norm(self.v - other.v)
    
    def copy(self):
        '''Makes a copy of a point.'''
        p = Point3D(self.v)
        return p
    
class Normal:
    def __init__(self, val, *args):
        if isinstance(val, numpy.ndarray):
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Normal")
        
    def __str__(self):
        return str(self.v)
    
    def __neg__(self):
        '''Negates a normal'''
        return Normal(self.v * -1 )  
        
    def __add__(self, other):
        '''Adds a normal and a normal, or a normal and a vector'''
        if isinstance(other, Normal):
            return Normal(self.v + other.v)
        elif isinstance(other, Vector3D):
            return Vector3D(self.v + other.v)   
        
    def __mul__(self, other):
        '''Multiply a normal by another vector, overload * operator'''
        if isinstance(other, Vector3D):
            return numpy.dot(self.v, other.v)
        else:
            return Normal(self.v * other)
    
    def dot(self, other):
        '''Find the dot product of two vectors'''
        return numpy.dot(self.v, other.v)
    
    def magnitude(self) :
        '''Return the magnitude of normal'''
        return numpy.linalg.norm(self.v)
    
    def __truediv__(self, other):
        '''Divide a Normal by a float'''
        return Normal(self.v / other)
    
 
class Ray:
    def __init__(self, origin, direction, *args):
        if isinstance(origin, Point3D) :
            self.origin = origin
        else:
            raise Exception("Invalid Arguments to Ray")
        if isinstance(direction, Vector3D) :
            self.direction = direction
        elif isinstance(direction, Normal):
            self.direction = direction
        else:
            raise Exception("Invalid Arguments to Ray")
   
    def copy(self): 
        '''Used to copy a Ray object'''
        r = Ray(self.origin, self.direction)
        return r
            
    def __repr__(self):
        '''Used to print Ray object in format [1,1,1,] [2,2,2]
        in order of origin and ray direction respectively'''
        return "[" + str(self.origin) + ", " + str(self.direction)+"]"
    
class ColorRGB: 
    def __init__(self, val, *args):
        if isinstance(val, numpy.ndarray):
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to ColorRGB")

    def copy(self):
        '''Makes a copy of a ColorRGB object.'''
        r = ColorRGB(self.v)
        return r
      
    def __repr__(self):
        '''Used to print ColorRGB object in format [1. 1. 1.]'''
        return str(self.v)
    
    def get(self):
        '''Used to return the individual RGB values back to functions.'''
        red, green, blue = self.v[0], self.v[1], self.v[2]
        return red, green, blue
      
    def __add__(self, other):
        '''Add 2 RGB objects'''
        return ColorRGB(self.v + other.v)   
        
    def __mul__(self, other):
        '''Multiply ColorRGB by float or another ColorRGB'''
        if isinstance(other, ColorRGB):
            return ColorRGB(self.v * other.v)
        else:
            return ColorRGB(self.v * other)
    
    def __truediv__(self, other):
        '''Divide a ColorRGB by a float'''
        return ColorRGB(self.v / other)

    def __pow__(self, other):
        '''Raise the individual color values to the value of the float.'''
        return ColorRGB(self.v**other)
    
class Plane:
    def __init__(self, point, normal, color=ColorRGB(1,1,1), *args):
        if isinstance(point, Point3D) :
            self.point = point
        else:
            raise Exception("Invalid Arguments to Plane")
        if isinstance(normal, Normal) :
            self.normal = normal
        else:
            raise Exception("Invalid Arguments to Plane")       
        if isinstance(color, ColorRGB) :
            self.color = color
        else:
            raise Exception("Invalid Arguments to Plane")   
          
    def copy(self):
        '''Makes a copy of a Plane object.'''
        p = Plane(self.point, self.normal, self.color)
        return p
    
    def __repr__(self):
        '''Used to print Plane object in format [1,1,1,] [2,2,2]
        in order of point and normal respectively'''
        return "[" + str(self.point) + ", " + str(self.normal)+"]"
    
    def hit(self, ray, epsilon, shadeRec=False):
        '''Used to find a hit point between the Ray and the Plane'''
        '''Note that epsilon is an extremely small number, 10^-6'''
        rayParameter = ((self.point - ray.origin)).dot(self.normal)/ray.direction.dot(self.normal)
        
        #Check if hit point will be valid. If t >= 0 valid.
        pointFound = False
        if(rayParameter >= 0):
           pointFound = True
           
        #Calculate hit point.
        hitPoint = ray.origin + ray.direction*rayParameter
        colorPlane = self.color
        return pointFound, rayParameter, hitPoint, colorPlane
    
    
class Sphere:
    def __init__(self, center, radius, color=ColorRGB(1,1,1), *args):
        if isinstance(center, Point3D) :
            self.center = center
        else:
            raise Exception("Invalid Arguments to Sphere")
        if isinstance(radius, float) :
            self.radius = radius
        elif isinstance(radius, int):
            self.radius = radius
        else:
            raise Exception("Invalid Arguments to Sphere")       
        if isinstance(color, ColorRGB) :
            self.color = color
        else:
            raise Exception("Invalid Arguments to Sphere")  
        
    def copy(self):
        '''Makes a copy of a Sphere object.'''
        p = Sphere(self.center, self.radius, self.color)
        return p
    
    def __repr__(self):
        '''Used to print Sphere object in format [[1,1,1,], 10.0]
        in order of point and radius respectively'''
        return "[" + self.center + ", " + (self.radius)+"]"
    
    def hit(self, ray, epsilon, shadeRec=False):
        '''Used to find a hit point between the Ray and the Plane'''
        '''Note that epsilon is an extremely small number, 10^-6'''
        a = ray.direction.dot(ray.direction)
        b = ((ray.origin-self.center)*2).dot(ray.direction)
        c = (ray.origin - self.center).dot(ray.origin-self.center) - (self.radius**2)
        d = (b*b)-(a*c*4)
        
        #Check if hit point will be valid. If d < 0 invalid.
        pointFound = False
        if(d>=0) :
            pointFound = True
            rayParameter = (-b - numpy.sqrt(d))/(2*(a))
            hitPoint = ray.origin + ray.direction*rayParameter
            colorPlane = self.color
            return pointFound, rayParameter, hitPoint, colorPlane
        else:
            rayParameter = (b - numpy.sqrt(-d))/(2*(a))
            hitPoint = ray.origin + ray.direction*rayParameter
            colorPlane = self.color
            return pointFound, rayParameter, hitPoint, colorPlane

        #Calculate hit point.
        
       
class ViewPlane:
    def __init__(self, center, normal, hres, vres, pixelSize, *args):
        if isinstance(center, Point3D) :
            self.center = center
        else:
            raise Exception("Invalid Arguments to ViewPlane")
        if isinstance(normal, Normal) :
            self.normal = normal
        else:
            raise Exception("Invalid Arguments to ViewPlane")       
        self.hres = hres
        self.vres = vres 
        self.pixelSize = pixelSize 
        
        #Create the 2D hres and vres array, fill with 0s. 
        self.vp = [] #GenAI usage #1
        for _ in range(vres):  # Rows (vertical)
            row = []
            for _ in range(hres):  # Columns (horizontal)
                row.append(ColorRGB(0,0,0))  # Default black: 0, 0, 0
            self.vp.append(row)
        
        #Find lower left.
        n = self.normal
        self.u = Vector3D(0,-1,0).cross(-n)/ Vector3D(0,-1,0).cross(-n).magnitude()
        self.v = self.u.cross(-n)
        c = self.center
        self.LL = c - self.u * self.hres/2.0 * self.pixelSize - self.v * self.vres/2.0 * self.pixelSize
        
    def get_color(self, row, col) :
        '''Retrieve the ColorRGB object located at position (x, y).'''
        return self.vp[row][col]
        
        
    def set_color(self, row, col, ColorRGB) : 
        '''Set a specific pixel's value to the ColorRGB object. '''
        self.vp[row][col] = ColorRGB
        
    def get_point(self, row, col) :
        '''Return a Point3D object that is located at the center
        of the specific pixel.'''
        p = self.LL + self.u * (col+0.5) * self.pixelSize + self.v * (row+0.5) * self.pixelSize
        return p
        
    def get_resolution(self) : 
        '''Retrieve the horizontal and vertical values for the 
        size of the viewing plane, this should return both 
        numbers back individually.'''
        return self.hres, self.vres
        
    def orthographic_ray(self, row, col) :
        '''Find the point at the center of a specific pixel 
        in the viewing plane. This can be considered the 
        ray's origin for the purposes of drawing our scene
        , use this point and the ViewPlane's normal to build 
        and return a Ray Object.'''
        p = self.get_point(row, col)
        return Ray(p, self.normal)
        

class PPM:
    def __init__(self, ViewPlaneObject, filename, *args):
        if isinstance(ViewPlaneObject, ViewPlane) :
            self.ViewPlaneObject = ViewPlaneObject
        else:
            raise Exception("Invalid Arguments to PPM")
        if isinstance(filename, str) :
            self.filename = filename
        else:
            raise Exception("Invalid Arguments to PPM")       
        self.hres, self.vres = self.ViewPlaneObject.get_resolution()
        #print(self.hres)
        #print(self.vres)
        
        with open(filename, "w") as f: #GenAI 2
            f.write("P3\n")  # PPM magic number
            f.write(f"{self.hres} {self.vres}\n")  # Image dimensions
            f.write(f"{255}\n")  # Maximum color value
            
            for y in reversed(range(self.vres)):
                for x in range(self.hres):
                    red, green, blue = self.ViewPlaneObject.get_color(y, x).get()
                    f.write(f"{int(red*255)} {int(green*255)} {int(blue*255)} ")  # RGB values (red, green, blue)
                f.write("\n")

    
        
         
#Library Debugging
if __name__ == '__main__':
    u = Vector3D(2,2,4)
    v = Vector3D(4,5,6)
    p1 = Point3D(1,1,-10)
    p2 = Point3D(2,4,2)
    n = Normal(-3,-3,-2)
    c = p1-p2
    col = ColorRGB(1,0,1)
    ray = Ray(p1, u)
    plane = Plane(p2, n)
    #print(p1)
    hit = Sphere(Point3D(0,0,0), 10.0).hit(Ray(Point3D(2,2,-20), Vector3D(0,0,1)), 0.000001)
    #print(hit)
    view = ViewPlane(Point3D(0,0,0), Normal(1,1,-1), 640, 480, 1)
    p = view.get_point(250, 100)
    print(p)
    r= view.orthographic_ray(250,100)
    print(r)
    view.get_color(250,100)
    PPM(view,'part3-testing.ppm')
    '''vp = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1.0)
    print(str(['debug 1',0,0,vp.get_point(0,0)]))
    print(str(['debug 2',479,639,vp.get_point(479,639)]))'''