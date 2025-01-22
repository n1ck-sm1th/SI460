#Nicholas Smith
#265904

from graphics import * 

def main():
    
    #Point, normal, camera, and direction initialization.
    p = Point3D(1,1,1) 
    n = Normal(-3, -3, -2)
    camera = Point3D(1, 1, -10)
    d = Vector3D(2, 2, 4)
    
    plane = Plane(p, n)
    print(plane)   
    
if __name__=="__main__":
    main()