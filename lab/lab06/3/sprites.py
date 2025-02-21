# SI460 pyglet sprite loading library

# pyglet and system libraries
import pyglet, os
import re

# Function to load all images from all subdirs in sprite directory
# Returns a dictionary of the form:
#    {'hero': {'Run':{'Left':  [...array of images facing left...],
#                     'Right': [...array of images facing right...]}}}
def loadAllImages(filepath="mylevel/sprites"):
    pass

# Function to load all images within a subdirectory
# Returns a dictionary of the form:
#    {'Run':{'Left':  [...array of images facing left...],
#            'Right': [...array of images facing right...]}}
def loadImages(filepath="mylevel/sprites/hero"):
    files = os.listdir(filepath)
    files.sort(key=natural_keys)
    left = []
    for file in files:
        line = file.split(' ')
        print(line[0])
        #left.append(file)
        # process files by class (Attack, Climb, Dead, etc as you find them, don't hardcode this in)
    for i in left:
        print(i)
    pass

# Build and return a configured sprite
def buildSprite(sprites={}, character="hero", mode="Run", facing="Right",
                animationSpeed=0.05, animationScale=0.15, animationLoop=True,
                animationX=400, animationY=300):
    pass

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def atoi(text):
    return int(text) if text.isdigit() else text.lower()


# Run the following code if this script was run directly from the command line
if __name__ == '__main__':
    loadTest = loadImages()
    imagesTest = loadAllImages()
