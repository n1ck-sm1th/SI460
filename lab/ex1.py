#!/usr/bin/python3

import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *

class Scene:

    # Initialize and run our environment
    def __init__(self, width=800, height=600, caption="Would you like to play a game?", resizable=False):

        # Build the OpenGL / Pyglet Window
        self.window = pyglet.window.Window(width=width, height=height, resizable=resizable, caption=caption)

        # Fix transparent issue...
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Event Handler for drawing the screen
        @self.window.event
        def on_draw():
            self.window.clear()

            glViewport(0, 0, width, height)
            glMatrixMode(gl.GL_PROJECTION)
            glLoadIdentity()
            #glOrtho(0, width, 0, height, -1, 1)
            #You can move the Frustrum as well to help move the objec.
            #This is the camera. 
            glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 100.0)
            glMatrixMode(gl.GL_MODELVIEW)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            #Resets, loads the identity matrix. 
            glLoadIdentity()

            glColor3f(1.0, 1.0, 1.0)
            
            #Function that is pushing the cube around. More - in z 
            #direction will push cube further into the scene. 
            glTranslatef(0.0, 0.0, -20.0)
            #Draw a new wireCube. 
            WireCube(5)
            #Saling rotation, transltion.
            WireCube(0.5)

        def WireCube(dim):
            x_min, y_min, z_min = -0.5*dim, -0.5*dim, -0.5*dim
            x_max, y_max, z_max =  0.5*dim,  0.5*dim,  0.5*dim
            glBegin(GL_LINE_STRIP)
            glVertex3f(x_min, y_min, z_min)
            glVertex3f(x_max, y_min, z_min)
            glVertex3f(x_max, y_max, z_min)
            glVertex3f(x_min, y_max, z_min)
            glVertex3f(x_min, y_min, z_min)
            glVertex3f(x_min, y_min, z_max)
            glVertex3f(x_max, y_min, z_max)
            glVertex3f(x_max, y_max, z_max)
            glVertex3f(x_min, y_max, z_max)
            glVertex3f(x_min, y_min, z_max)
            glVertex3f(x_min, y_max, z_max)
            glVertex3f(x_min, y_max, z_min)
            glVertex3f(x_max, y_max, z_min)
            glVertex3f(x_max, y_max, z_max)
            glVertex3f(x_max, y_min, z_max)
            glVertex3f(x_max, y_min, z_min)
            glEnd()

# Run the following code if this script was run directly from the command line
if __name__ == '__main__':
    myGame = Scene(600, 500, "Etch a Sketch")
    debugging = pyglet.window.event.WindowEventLogger()
    myGame.window.push_handlers(debugging)
    pyglet.app.run()
