#!/usr/bin/python3

import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *
import numpy

# Our OpenGL Graphical Environment!
class Scene:

    class eventStore:
        event = []
        i = 0
        clickSwitch = False
        
        def store(self, x):
            self.event.append(x)
    
    events = eventStore()
    # Initialize and run our environment
    def __init__(self, width=600, height=500, caption="Lab 5 - Etch-a-Sketch", resizable=False):
        
        # Build the OpenGL / Pyglet Window
        self.window = pyglet.window.Window(width=width, height=height, resizable=resizable, caption=caption)

        # Fix transparency issue...
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        #Track the motion of the mouse.
        @self.window.event
        def on_mouse_motion(x, y, dx, dy):
            print(str(['motion', x, y, dx, dy]))
        
        #Track when the mouse is dragged and held. 
        @self.window.event
        def on_mouse_drag(x, y, dx, dy, button, mod):
            print(str(['drag', x, y, dx, dy]))
            if self.events.clickSwitch == True:
                self.events.store(['drag', x, y])
        
        #Track when mosuse is pressed. 
        @self.window.event
        def on_mouse_press(x, y, dx, dy):
            print(str(['mouse', x, y]))
            #self.events.store(['mouse', x, y])
            self.events.clickSwitch = True
 
        #Track when mouse is released.
        @self.window.event
        def on_mouse_release(x, y, dx, dy):
            print(str(['release', x, y]))
            #self.events.store(['release', x, y])
            self.events.clickSwitch = False

        # Resize our world based on the size of the window, in many cases
        # it's not in your best interest to allow resizing.
        @self.window.event
        def on_resize(width, height):
            glViewport(0, 0, width, height)
            glMatrixMode(gl.GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, width, 0, height, -1, 1)
            glMatrixMode(gl.GL_MODELVIEW)

        # Event Handler for drawing the screen
        @self.window.event
        def on_draw():
            self.window.clear()

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            #Circle 1
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_TRIANGLE_FAN)
            howMany = 50
            for i in range(0, 360, int(360/howMany)):
                theta = numpy.radians(i)
                glColor3f(1.0, 1.0, 1.0)   # White
                glVertex3f(50 + 40 * numpy.cos(theta), 50 + 40 * numpy.sin(theta), 0.0)
            glEnd()
            
            #Circle 2
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_TRIANGLE_FAN)
            howMany = 50
            for i in range(0, 360, int(360/howMany)):
                theta = numpy.radians(i)
                glColor3f(1.0, 1.0, 1.0)   # White
                glVertex3f(550 + 40 * numpy.cos(theta), 50 + 40 * numpy.sin(theta), 0.0)
            glEnd()

            #Box
            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_LINES)
            glVertex3f(100, 100, 0)
            glVertex3f(500, 100,0)
            glVertex3f(500, 450,0)
            glVertex3f(100, 450, 0)
            glVertex3f(500, 100,0)
            glVertex3f(500, 450,0)
            glVertex3f(100, 100, 0)
            glVertex3f(100, 450, 0)
            glEnd()

            #Label
            label = pyglet.text.Label('Etch A Sketch',
            font_name='Times New Roman',
            font_size=24,
            x=300, y=470,
            anchor_x='center', anchor_y='center')
            label.draw()

            glColor3f(1.0, 1.0, 1.0)
            glBegin(GL_LINES)
            for i in self.events.event:
                glVertex3f(i[1], i[2], 0.0)   
            glEnd() 

           

# Run the following code if this script was run directly from the command line
if __name__ == '__main__':
    myGame = Scene(600, 500, "Etch a Sketch", True)
    #debugging = pyglet.window.event.WindowEventLogger()
    #myGame.window.push_handlers(debugging)
    pyglet.app.run()