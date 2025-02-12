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
    
    points = [float(p) for p in points] 

    glColor3f(1.0, 1.0, 1.0)   # White
    if primitive == "GL_LINES":
        glBegin(GL_LINES)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd()
    elif primitive == "GL_POINTS":
        glBegin(GL_POINTS)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd()   
    elif primitive == "GL_LINE_STRIP":
        glBegin(GL_LINE_STRIP)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd()   
    elif primitive == "GL_LINE_LOOP":
        glBegin(GL_LINE_LOOP)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd() 
    elif primitive == "GL_TRIANGLES":
        glBegin(GL_TRIANGLES)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd() 
    elif primitive == "GL_TRIANGLE_STRIP":
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd() 
    elif primitive == "GL_TRIANGLE_FAN":
        glBegin(GL_TRIANGLE_FAN)
        for i in range(0, len(points) -1 , 2):
            glVertex2f(points[i], points[i+1])
        glEnd()
    
    
pyglet.app.run()