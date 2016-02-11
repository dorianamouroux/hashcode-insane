# insane team

class Drone:
    
    def __init__(self, id):
        self.x = 0
        self.y = 0
        self.id = id
    
    def getId(self):
        return self.id
    
    def getX(self):
        return (self.x)
    
    def getY(self):
        return (self.y)
        
    def setX(self, x):
        self.x = x
        
    def setY(self, y):
        self.y = y
    
    def toString(self):
        print("I'm a drone (id=%d) in position <%d,%d>" % (self.id, self.x, self.y))