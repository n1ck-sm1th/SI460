#!/usr/bin/python3

# Load in the appropriate pyglet libraries
import pyglet
from pyglet.gl import *

# Define the window
window = pyglet.window.Window(400, 400, resizable=False, caption='ex1.py')

# Define how we should draw whats inside the window
@window.event
def on_draw():
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 100.0, 0.0, 100.0, -2.0, 1.0)
    glMatrixMode(gl.GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 1.0, 1.0)   # White

    glBegin(GL_TRIANGLES)
    glVertex3f(10.0, 10.0, 0.0)
    glVertex3f(60.0, 10.0, 0.0)
    glVertex3f(60.0, 60.0, 0.0)
    glEnd()

    glColor3f(0.79, 0.19, 0.99)   # Purple
    
    glBegin(GL_TRIANGLES)
    glVertex3f(45.0, 10.0, 0.0)
    glVertex3f(85.0, 10.0, 0.0)
    glVertex3f(85.0, 85.0, 0.0)
    glEnd()

    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)   # Red
    glVertex3f(8.0, 8.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)    # Green
    glVertex3f(62.0, 8.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)    # Blue
    glVertex3f(62.0, 62.0, 0.0)
    glColor3f(1.0, 1.0, 0.0)    # Yellow
    glVertex3f(8.0, 62.0, 0.0)
    glEnd()

# Begin the main program loop
pyglet.app.run()