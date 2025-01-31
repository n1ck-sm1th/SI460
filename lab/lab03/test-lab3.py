# Prevents the creation of .pyc files
import sys, traceback, numpy
sys.dont_write_bytecode = True

# Initialize variables
c,u,v,n,m,a,b = None, None, None, None, None, None, None

# Load in classes
try:
    from graphics import Point3D
except:
    print("FAIL - NO Point3D Class")

try:
    from graphics import Vector3D
except:
    print("FAIL - NO Vector3D Class")

try:
    from graphics import Normal
except:
    print("FAIL - NO Normal Class")

try:
    from graphics import Ray
except:
    print("FAIL - NO Ray Class")

try:
    from graphics import ColorRGB
except:
    print("FAIL - NO ColorRGB Class")

try:
    from graphics import Plane
except:
    print("FAIL - NO Plane Class")


# Create Variables
try:
    TEST = "Creating Vector3Ds"
    v = Vector3D(1,2,3)
    u = Vector3D(4,5,6)
    print ("PASS "+TEST)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print ("FAIL "+TEST+" ("+str(e)+")")
    myerror = traceback.format_tb(exc_traceback)
    for line in myerror:
        line = str(line).split('\n')
        for item in line:
            print("ERROR: "+item)

try:
    TEST = "Creating Point3Ds"
    a = Point3D(1,3,5)
    b = Point3D(2,5,6)
    print ("PASS "+TEST)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print ("FAIL "+TEST+" ("+str(e)+")")
    myerror = traceback.format_tb(exc_traceback)
    for line in myerror:
        line = str(line).split('\n')
        for item in line:
            print("ERROR: "+item)

try:
    TEST = "Creating Normals"
    n = Normal(5,3,1)
    m = Normal(6,4,2)
    print ("PASS "+TEST)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print ("FAIL "+TEST+" ("+str(e)+")")
    myerror = traceback.format_tb(exc_traceback)
    for line in myerror:
        line = str(line).split('\n')
        for item in line:
            print("ERROR: "+item)

try:
    TEST = "Creating Rays"
    ro1 = Point3D(0,0,0)
    rv1 = Vector3D(1,1,1)
    ro2 = Point3D(1,1,-10)
    rv2 = Vector3D(2,2,4)
    r1 = Ray(ro1, rv1)
    r2 = Ray(ro2, rv2)
    print ("PASS "+TEST)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print ("FAIL "+TEST+" ("+str(e)+")")
    myerror = traceback.format_tb(exc_traceback)
    for line in myerror:
        line = str(line).split('\n')
        for item in line:
            print("ERROR: "+item)

try:
    TEST = "Creating Colors"
    c0 = ColorRGB(0,0,0)
    c1 = ColorRGB(1,1,1)
    c2 = ColorRGB(0.2,0.4,0.9)
    c3 = ColorRGB(0.32,0.22,0.03)
    print ("PASS "+TEST)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print ("FAIL "+TEST+" ("+str(e)+")")
    myerror = traceback.format_tb(exc_traceback)
    for line in myerror:
        line = str(line).split('\n')
        for item in line:
            print("ERROR: "+item)

try:
    TEST = "Creating Planes"
    p0 = Point3D(2,4,2)
    n0 = Normal(-3,-3,-2)
    p = Plane(p0, n0)
    print ("PASS "+TEST)
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print ("FAIL "+TEST+" ("+str(e)+")")
    myerror = traceback.format_tb(exc_traceback)
    for line in myerror:
        line = str(line).split('\n')
        for item in line:
            print("ERROR: "+item)


# Return the string value (protected by try)
def show(t):
    try:
        return str(numpy.round(t,2))
    except:
        try:
            return str(numpy.around(t, decimals=4))
        except:
            try:
                return str(numpy.around(t.v, decimals=4))
            except:
                try:
                    return str(t)
                except:
                    return 'INVALID STRING'

# Evaluate for errors
def test(TEST, c0, c1, c2, c3):
    try:
        t = eval(TEST)
        print (">>>> "+TEST.ljust(20)+' => '+show(t))
        return t
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print ("FAIL "+TEST+" ("+str(e)+")")
        myerror = traceback.format_tb(exc_traceback)
        for line in myerror:
            line = str(line).split('\n')
            for item in line:
                print("ERROR: "+item)
        return None


# Running Lab 3 Tests now for hitpoints...


# Part2
# Color Tests
t = test('c0+c1', c0, c1 , c2, c3)
t = test('c0+c2', c0, c1 , c2, c3)
t = test('c3+c2', c0, c1 , c2, c3)
t = test('c2*2', c0, c1 , c2, c3)
t = test('c3*3', c0, c1 , c2, c3)
t = test('c2/2', c0, c1 , c2, c3)
t = test('c3/3', c0, c1 , c2, c3)
t = test('c2.__pow__(2)', c0, c1 , c2, c3)
t = test('c3.__pow__(3)', c0, c1 , c2, c3)

#### Part5 Test
r = Ray(Point3D(0,0,-10), Vector3D(0.2,0.2,0.8))
p = Plane(Point3D(1,1,1), Normal(1,1,1))
results = list(p.hit(r, 0.001))
results[1] = round(results[1],5)
print(['Part5-test1','ray=',show(r),'point=',show(p)])
print([show(results)])

r = Ray(Point3D(0,0,-10), Vector3D(0.2,0.2,0.8))
p = Plane(Point3D(3,12,8), Normal(0.1,0.3,0.7))
results = list(p.hit(r, 0.001))
results[1] = round(results[1],5)
print(['Part5-test2','ray=',show(r),'point=',show(p)])
print([show(results)])

r = Ray(Point3D(0,0,-10), Vector3D(0.1,0.3,0.7))
p = Plane(Point3D(3,12,8), Normal(0.1,0.3,0.7))
results = list(p.hit(r, 0.001))
results[1] = round(results[1],5)
print(['Part5-test2','ray=',show(r),'point=',show(p)])
print([show(results)])
