#using screeninfo module here to allow to work on multiple OS rather than just windows. In makefile will have to include this as a dependancy.
from screeninfo import get_monitors

class Monitor:
    #Have an array with all current instances, can print length to find total number of these.
    instances = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Monitor.instances.append(self)

    def __str__(self):
        return f"Monitor width: {self.width} Monitor height: {self.height}"

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
monitorArray = []
widthArray = []
heightArray = []

i = 0
#Get screen resolution dynamically
for monitor in get_monitors():
    monitorArray.append(Monitor(monitor.width, monitor.height))
    widthArray.append(monitorArray[0].getWidth())
    heightArray.append(monitorArray[0].getHeight())


#These are our defined constants for screen height and size. Will always return the smallest screensize provided becuase otherwise we risk making a massive window for a tiny screen.
SCREEN_WIDTH = min(widthArray)
SCREEN_HEIGHT = min(heightArray)
        
