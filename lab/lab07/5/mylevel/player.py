#!/usr/bin/python3

# Important Libraries
import pyglet, config

# Our Hero Class
class Player:
    def __init__(self, sprites={},
                       buildSprite=None,
                       playerClass="hero",
                       mode="Run",
                       facing="Right",
                       speed=0.05,
                       scale=0.15,
                       loop=True,
                       x=380,
                       y=250):

        # Store the sprites, and the sprite building function
        self.sprites      = sprites
        self.buildSprite  = buildSprite
        self.playerSprite = None

        # Some basic settings
        self.animationSpeed = speed
        self.animationScale = scale
        self.animationLoop  = loop
        self.animationX     = x
        self.animationY     = y
        self.playerClass    = playerClass
        self.mode           = mode
        self.facing         = facing

        # Build the starting character sprite
        self.changeSprite()

    # Build the initial character
    def changeSprite(self, mode=None, facing=None):
        if mode is not None:
            self.mode = mode
        if facing is not None:
            self.facing = facing
        if self.playerSprite is not None:
            self.animationX = self.playerSprite.x
            self.animationY = self.playerSprite.y
        self.playerSprite = self.buildSprite(self.sprites,
                                             self.playerClass,
                                             self.mode,
                                             self.facing,
                                             self.animationSpeed,
                                             self.animationScale,
                                             self.animationLoop,
                                             self.animationX,
                                             self.animationY)

    # Move the character
    def movement(self, t=0, keyTracking={}):
        modifiers = False
        if pyglet.window.key.LSHIFT in keyTracking or pyglet.window.key.RSHIFT in keyTracking:
            modifiers = True
        
        #Right movement.
        if pyglet.window.key.RIGHT in keyTracking:
            if modifiers & pyglet.window.key.MOD_SHIFT: # Check if shift is held
                self.playerSprite.x += 9
            else:
                self.playerSprite.x += 3
            if self.mode != 'Run':
                self.mode = 'Run'
                if self.facing != 'Right':
                    self.facing = 'Right'
                self.changeSprite()
            
        #Left movement.
        elif pyglet.window.key.LEFT in keyTracking:
            if modifiers & pyglet.window.key.MOD_SHIFT: # Check if shift is held
                self.playerSprite.x -= 9
            else:
                self.playerSprite.x -= 3
            if self.mode != 'Run':
                self.mode = 'Run'
                if self.facing != 'Left':
                    self.facing = 'Left'
                self.changeSprite()

       
            #If there are no buttons being pressed. 
        elif self.mode != 'Idle':
                self.mode = 'Idle'
                self.changeSprite()
        
    # Draw our character
    def draw(self, t=0, keyTracking={}, *other):
        self.movement(t, keyTracking)
        self.playerSprite.draw()