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

# Return the string value (protected by try)
def show(t):
    try:
        return str(numpy.round(t,2))
    except:
        try:
            return str(numpy.around(t, 2))
        except:
            try:
                return str(t)
            except:
                return 'INVALID STRING'

# Evaluate for errors
def test(TEST, c, u, v, a, b, n, m):
    try:
        t = eval(TEST)
        print ("PASS "+TEST.ljust(20)+' => '+show(t))
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

# Lab Tests

c = 2.0

# Variable settings (reminder)
# v = Vector3D(1,2,3)
# u = Vector3D(4,5,6)
#
# a = Point3D(1,3,5)
# b = Point3D(2,5,6)
#
# n = Normal(5,3,1)
# m = Normal(6,4,2)

# Vector Tests
t = test('u+v',c,u,v,a,b,n,m)
t = test('u-v',c,u,v,a,b,n,m)
t = test('u*c',c,u,v,a,b,n,m)
t = test('u.magnitude()',c,u,v,a,b,n,m)
t = test('u.square()',c,u,v,a,b,n,m)
t = test('u.dot(v)',c,u,v,a,b,n,m)
t = test('u.cross(v)',c,u,v,a,b,n,m)

#Point Tests
t = test('a+u',c,u,v,a,b,n,m)
t = test('a-u',c,u,v,a,b,n,m)
t = test('a-b',c,u,v,a,b,n,m)
t = test('a.distance(b)',c,u,v,a,b,n,m)
t = test('a.distancesquared(b)',c,u,v,a,b,n,m)
t = test('a*c',c,u,v,a,b,n,m)

# Normal Tests
t = test('-n',c,u,v,a,b,n,m)
t = test('n+m',c,u,v,a,b,n,m)
t = test('n.dot(u)',c,u,v,a,b,n,m)
t = test('n*c',c,u,v,a,b,n,m)
t = test('n+u',c,u,v,a,b,n,m)
t = test('u+n',c,u,v,a,b,n,m)