#!/usr/bin/python3

import pyglet
from pyglet.gl import gl
import numpy
import sys

# Create the window
window = pyglet.window.Window(400, 400, "Nicholas Smith 265904")

@window.event
def on_draw(): 
    gl.glMatrixMode(gl.GL_PROJECTION) 
    gl.glLoadIdentity()  
    gl.glOrtho(0, 100, 0, 100, -2, 1)  
    gl.glMatrixMode(gl.GL_MODELVIEW)  
    gl.glLoadIdentity()
    
    vertices = int(sys.argv[1])
    gl.glBegin(gl.GL_LINE_LOOP)
    for i in range(vertices):
        angle = 2 * numpy.pi * i / vertices
        x = 50 + 25 * numpy.cos(angle)
        y = 50 + 25 * numpy.sin(angle)
        gl.glVertex2f(x, y)
    gl.glEnd()
    
pyglet.app.run()