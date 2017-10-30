global cWidth  
global cHeight
cWidth = 600  #global canvas width
cHeight = 600 #global canvas height
class player(object):              # will run when an instance class/object is created or called
    def __init__(self):            # works same as initialization/ it initializes the object  
        self.x = 0              # Starting position of our sprite in x-axis
        self.y = 0              # # Starting position of our sprite in y-axis
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        self.speed = 1
        self.h = 20
        self.w = 20
        
    def show(self):               # method in class player. 
        fill(0)
        rect(self.x,self.y,self.w,self.h)  # our sprite shape is rectangle with (x-position,y-position,width,height)
        
    def update(self):
        self.x = self.x + (self.right - self.left) * self.speed  # whenever button pressed it will update the sprite x-position
        self.y = self.y + (self.down - self.up) * self.speed     # whenever button pressed it will update the sprite y-position   
        if not (self.x >= 0):   # If sprite goes out of the window it will reset itswidth position
            self.x = 0
        if not (self.x <= (cWidth - self.w)): 
            self.x = (cWidth - self.w)
        if not (self.y >= 0):    #If sprite goes out of the window it will reset its height position
            self.y = 0
        if not (self.y <= (cHeight - self.h)):
            self.y = (cHeight - self.h)

def setup():
    size(cWidth,cHeight)
    global p
    p = player()       # instance class/object p is an object which is just an instance of player
    
def draw():              #draw function will run constantly over the screen
    background(100)      # It will not leave the trail behind the sprite.
    p.show()             # it shows our sprite in the window
    p.update()
    
def keyPressed():               # built in function in processing
    if keyCode == UP:           # keyCode indicates the arrow key       
        p.up = 1
    if keyCode == DOWN:
        p.down = 1
    if keyCode == LEFT:
        p.left = 1
    if keyCode == RIGHT:
        p.right = 1
        
def keyReleased():              # built in function in processing
    if keyCode == UP:           # keyCode indicates the arrow key
        p.up = 0
    if keyCode == DOWN:
        p.down = 0
    if keyCode == LEFT:
        p.left = 0
    if keyCode == RIGHT:
        p.right = 0 