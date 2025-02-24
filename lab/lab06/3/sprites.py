# SI460 pyglet sprite loading library

# pyglet and system libraries
import pyglet, os
import re

# Function to load all images from all subdirs in sprite directory
# Returns a dictionary of the form:
#    {'hero': {'Run':{'Left':  [...array of images facing left...],
#                     'Right': [...array of images facing right...]}}}
def loadAllImages(filepath="mylevel/sprites"):
    dirs = os.listdir(filepath)
    a =  loadImages()
    allImages = {}
    for obj in dirs:
        if obj not in dirs:
            allImages[obj].append(a)
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
    loadTest = loadAllImages()
    #Gen AI 2
    '''for action, directions in loadTest.items():
        print(f"'{action}': ")  # Print the action key
        for direction, image_list in directions.items():
            print(f"    '{direction}': {image_list},")  # Print the direction and image list
        print("}")  # Close the action dictionary'''
    for obj, action, directions in loadTest:
        print(f"'{obj}': ")  # Print the action key
        #for action, directions in loadTest.items():
            #print(f"'{action}': ")  # Print the action key
            #for direction, image_list in directions.items():
                #print(f"    '{direction}': {image_list},")  # Print the direction and image list
            #print("}")  # Close the action dictionary
    #imagesTest = loadAllImages()
