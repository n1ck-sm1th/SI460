#Nicholas Smith
#265904

from graphics import * 

def findRayParameter(plane, ray):
    #Calculate ray parameter using equation t = (a-o)*n/(d*n)
    return ((plane.point - ray.origin)).dot(plane.normal)/ray.direction.dot(plane.normal)

def main():
    
    plane1 = Plane(Point3D(0,0,5), Normal(0,0,1)) 
    plane2 = Plane(Point3D(0,0,20), Normal(0,0,1))
    point1 = Point3D(1,1,5) 
    point2 = Point3D(1,2,5) 
    point3 = Point3D(2,1,5) 
    point4 = Point3D(2,2,5) 
    origin = Point3D(0,0,0)
    ray1 = Ray(origin, Vector3D(1,1,5))
    ray2 = Ray(origin, Vector3D(1,2,5))
    ray3 = Ray(origin, Vector3D(2,1,5))
    ray4 = Ray(origin, Vector3D(2,2,5))
    #Point 1 [4, 4, 20]
    t1 = findRayParameter(plane2, ray1)
    f1 = origin + point1*t1
    print(f1)
    
    #Point 2 [4, 8, 20]
    t2 = findRayParameter(plane2, ray2)
    f2 = origin + point2*t2
    print(f2)
    
    #Point 3 [8, 4, 20]
    t3 = findRayParameter(plane2, ray3)
    f3 = origin + point3*t3
    print(f3)
    
    #Point 4 [8, 8, 20]
    t4 = findRayParameter(plane2, ray4)
    f4 = origin + point4*t4
    print(f4)
    
    
    #Ray equation p = o + td 

    #Plane equation (o + td-a) * n = 0
    
    '''We reorder the dt to td because in our Vector Class we do
    not have a way to multiply a Vector3D when it is on the right
    side of an operator.'''
    #final = camera + d*rayParameter
       
    
if __name__=="__main__":
    main()