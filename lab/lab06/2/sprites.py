# SI460 pyglet sprite loading library

# pyglet and system libraries
import pyglet, os
import re
import json

# Function to load all images from all subdirs in sprite directory
# Returns a dictionary of the form:
#    {'hero': {'Run':{'Left':  [...array of images facing left...],
#                     'Right': [...array of images facing right...]}}}
def loadAllImages(filepath="mylevel/sprites"):
    dirs = os.listdir(filepath) #Gen AI 3
    allImages = {}
    for obj in dirs:
        full_obj_path = os.path.join(filepath, obj)
        if os.path.isdir(full_obj_path): # Ensure it's a directory
            allImages[obj] = loadImages(full_obj_path)
    return allImages

# Function to load all images within a subdirectory
# Returns a dictionary of the form:
#    {'Run':{'Left':  [...array of images facing left...],
#            'Right': [...array of images facing right...]}}
def loadImages(filepath="mylevel/sprites/hero"):
    files = os.listdir(filepath)
    files.sort(key=natural_keys)
    images = {} #Gen AI 1
    for file in files:
        line = file.split(' ')
        action = line[0]
        directionL = 'Left'
        directionR = 'Right'
    
        if action not in images:
            images[action] = {'Left': [], 'Right': []}

        images[action][directionL].append(os.path.join(filepath, file))
        images[action][directionR].append(os.path.join(filepath, file))
    return images

# Build and return a configured sprite
def buildSprite(sprites={}, character="hero", mode="Throw", facing="Right",
                animationSpeed=0.05, animationScale=0.15, animationLoop=True,
                animationX=400, animationY=300):
    allImages = loadAllImages()
    playerSequence = []
    #print(allImages[character][mode][facing])
    for a in allImages[character][mode][facing]:
        playerSequence.append(pyglet.image.load(a))
    #print(playerSequence)
    playerAnimation = pyglet.image.Animation.from_image_sequence(playerSequence,
                                                             animationSpeed,
                                                             animationLoop)
    # Create the sprite from the animation sequence
    playerSprite = pyglet.sprite.Sprite(playerAnimation,
                                        x=animationX,
                                        y=animationY)
    playerSprite.scale = animationScale
    return playerSprite     

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def atoi(text):
    return int(text) if text.isdigit() else text.lower()


# Run the following code if this script was run directly from the command line
if __name__ == '__main__':
    loadTest = loadAllImages()
    loadTest1 = loadImages()
    #Gen AI 2
    # Print in the desired format
    #Part 4
    #print(json.dumps(loadTest, indent=4))
    playerSprite = buildSprite()
    playerSprite.draw()
    #Part 3
    #print(json.dumps(loadTest1, indent=4))
    #imagesTest = loadAllImages()