#!/usr/bin/python3

# Load in the appropriate pyglet libraries
import pyglet
from pyglet.gl import *
import math

# Define the window
window = pyglet.window.Window(400, 400, resizable=False, caption='example.py')

# Define how we should draw whats inside the window
@window.event
def on_draw():
    glMatrixMode(gl.GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-50.0,50.0,-50.0,50.0,30.0,100.0)

    glMatrixMode(gl.GL_MODELVIEW)
    glLoadIdentity()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glEnable(GL_DEPTH_TEST)

    glColor3f(1.0, 1.0, 1.0)   # White

    glBegin(GL_LINES)
    glVertex3f(-40,0,-40)
    glVertex3f(40,0,-40)
    glVertex3f(0,-40,-40)
    glVertex3f(0,40,-40)
    glEnd()

    glColor3f(0.6, 0.6, 0.6)   # Gray
    glBegin(GL_TRIANGLE_STRIP)
    glVertex3f(-30,25,-40)
    glVertex3f(-2,25,-35)
    glVertex3f(-2,28,-30)
    glEnd()

    glColor3f(0.79, 0.19, 0.99)   # Purple
    glBegin(GL_LINE_STRIP)
    x = -30.0
    step = 0.005
    while x < 30.0:
        x = x + step
        y = 30.0 * math.sin(x/3.0) + 8.0
        glVertex3f(x,y,-37.0)
        glVertex3f(x,y,-33.0)
        print(str([x,y]))
    glEnd()

    glDisable(GL_DEPTH_TEST)

# Begin the main program loop
pyglet.app.run()
