Part 1: Transformaitons
Case 1: Cube is rotated right and sent back into the screen. 

Case 2:Cube is rotated right and sent back into the screen, however it is
at a higher position than case 1. 

Case 3: Cube is rotated right, and streched in its y axis, making it no longer
a cube. 

Case 4:Appears as a view of the cube from a bird's eye view. Or, the cube is rotated
towards the camera and slightly rotated on its z axis.

Part 2: Matrix Multiplication
1.0 0.0 0.0 0.0 
0.0 1.0 0.0 0.0
0.0 0.0 1.0 20.0
0.0  0.0 0.0 1.0

The actual order would have been 
rotate scale translate
I x translate x rotate x scale 

Part 3: Rotations
Sequence is:
glRotatef(45.0, 0.0, 0.0, 1.0)
glTranslatef(5.0, -6.0, 0.0)
glTranslatef(0.0, 0.0, -15.0) 

Part 4: Translations
Sequence is:
glTranslatef(5.0, 0.0, -15.0)
WireCube(5)
glTranslatef(-10.0, 0.0, 0.0)
WireCube(5)
glTranslatef(5.0, -6.0, 0.0)
WireCube(5)
glTranslatef(0.0, 12.0, 0.0)
WireCube(5)  
