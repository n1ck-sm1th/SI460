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
        '''Square the vector'''
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
    
 
class Ray:
    def __init__(self, origin, direction, *args):
        if isinstance(origin, Point3D) :
            self.origin = origin
        else:
            raise Exception("Invalid Arguments to Ray")
        if isinstance(direction, Vector3D) :
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
        return self.v
      
    def __add__(self, other):
        '''Add 2 RGB objects'''
        return ColorRGB(self.v + other.v)   
        
    def __mul__(self, other):
        '''Multiply ColorRGB by float or another ColorRGB'''
        if isinstance(other, ColorRGB):
            return ColorRGB(self.v * other.v)
        if isinstance(other, float):
            return ColorRGB(self.v * other)
    
    def __truediv__(self, other):
        '''Divide a ColorRGB by a float'''
        if isinstance(other, float):
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
    
# We should always have debugging in our libraries
# that run if the file is called from the command line
# vice from an import statement!
if __name__ == '__main__':
    u = Vector3D(1,2,3)
    v = Vector3D(4,5,6)
    p1 = Point3D(1,1,1)
    p2 = Point3D(2,2,2)
    n = Normal(1,2,3)
    c = p1-p2
    #print(n.__str__())
    #print(str(c))
    #r = Ray(p1, u)
    #print(r)
    #r.__repr__()
    #print(str(-n))
    #print(p1.__str__())
    #p3 = p1.distancesquared(p2)
    #print(str(p3))
    '''print("Testing Printing...")
    print(u.__str__())
    print(v.__str__())

    if str(u) != '[1. 2. 3.]':
        raise Exception("Printing Error!")
    print("Testing Addition...")
    c = u + v
    print(c)
    if str(c) != '[5. 7. 9.]':
        raise Exception("Addition Error!")
    print("Testing subtraction")
    c = u - v 
    if str(c) != '[-3. -3. -3.]':
        raise Exception("Sub Error!")
    print(str(c))
    print("Testing multiplication")
    c = u*2 
    if str(c) != '[2. 4. 6.]':
        raise Exception("mult Error!")
    print(str(c))'''
    '''print("Testing division")
    c = u/2
    if str(c) != '[0.5. 1.  1.5.]':
        raise Exception("div Error!")
    print(str(c))
    print("Testing magnitude")
    c = u.magnitude()
    scaled_frac1 = int(c * 10**10)
    scaled_frac2 = int(math.sqrt(14) * 10**10)
    if scaled_frac1 != scaled_frac2:
        raise Exception("mag Error!")
    print(str(c))
    print("Testing square")
    c = u.square()
    if c != 14:
        raise Exception("sqaure Error!")
    print(str(c))
    print("Testing dot product")
    c = u.dot(v)
    if c != 32:
      raise Exception("dot Error!")
    print(str(c))
    print("Testing dot product")
    c = u * v 
    if c != 32:
      raise Exception("dot Error!")
    print(str(c))
    print("Testing dot angle")
    c = u.dotangle(v, 0) 
    scaled_frac1 = int(c * 10**10)
    scaled_frac2 = int(32.83291031876401 * 10**10)
    if scaled_frac1 != scaled_frac2:
      raise Exception("angle Error!")
    print(str(c))'''
    '''print("Testing cross product")
    c = u.cross(v) 
    if str(c) != '[-3.  6. -3.]':
      raise Exception("cross Error!")
    print(str(c))'''
