#Nicholas Smith
#265904

from graphics import * 

def main():
    
    #Point, normal, camera, and direction initialization.
    p = Point3D(2,4,2) 
    n = Normal(-3, -3, -2)
    camera = Point3D(1, 1, -10)
    d = Vector3D(2, 2, 4)
    origin = Point3D(0,0,0)
    
    #Ray initialization
    #Ray equation p = o + td 
    #st. t = ray parameter, unit vector d, p = specific point.
    ray = Ray(camera, d)
    
    #Plane initialization
    #Plane equation (o + td-a) * n = 0
    #Combinding ray and plane we can find intersection point.
    plane = Plane(p, n)
    
    #Calculate ray parameter using equation t = (a-o)*n/(d*n)
    rayParameter = ((p - camera)).dot(n)/d.dot(n)
    
    #Ray parameter check. t= 1.8
    #print(rayParameter)
    
    '''We reorder the dt to td because in our Vector Class we do
    not have a way to multiply a Vector3D when it is on the right
    side of an operator.'''
    final = origin + d*rayParameter
    
    #Final check Point = [3.6 3.6 7.2]
    
    #print(final)
    
       
    
if __name__=="__main__":
    main()