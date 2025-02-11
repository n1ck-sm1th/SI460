#!/usr/bin/python3

import pyglet
from pyglet.gl import *
import numpy
import sys

# Create the window
window = pyglet.window.Window(400, 400, "Nicholas Smith 265904")

@window.event
def on_draw(): 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()  
    glOrtho(0, 100, 0, 100, -2, 1)  
    glMatrixMode(GL_MODELVIEW)  
    glLoadIdentity()
    
    primitive = sys.argv[-1]
    points = sys.argv[1:-1]

    glColor3f(1.0, 1.0, 1.0)   # White
    if primitive == "GL_LINES":
        glBegin(GL_LINES)
        for i in range(0, len(points), 2):
            glVertex2f(float(points[i]), float(points[i+1])) 
        glEnd()
    
    #GL_POINTS
    
    #GL_LINES
    
    #GL_LINE_STRIP
    
    #GL_LINE_LOOP
    
    #GL_TRIANGLES
    
    #GL_TRIANGLE_STRIP
    
    #GL_TRIANGLE_FAN
    
    
pyglet.app.run()