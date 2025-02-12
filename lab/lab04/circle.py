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
    glOrtho(0.0, 100.0, 0.0, 100.0, -2.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    glColor3f(1.0, 1.0, 1.0) #White
    vertices = int(sys.argv[1])
    glBegin(GL_LINE_LOOP)
    for i in range(vertices):
        angle = 2 * numpy.pi * i / vertices
        x = 50 + 25 * numpy.cos(angle)
        y = 50 + 25 * numpy.sin(angle)
        glVertex3f(x, y, 0.0)
    glEnd()
    
pyglet.app.run()