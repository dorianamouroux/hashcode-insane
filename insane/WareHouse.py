# insane team

class WareHouse:
    
    def __init__(self, posX, posY, id):
        self.x = posX
        self.y = posY
        self.id = id
        self.products = []
    
    def addProduct(self, product):
        self.products.append(product)
    
    def hasProduct(self, id):
        for x in self.products:
            if x.getId() == id:
                return true
        return false
    
    def addProduct(self, product)
        self.products.append(product)
    
    def toString(self):
        print("I am a warehouse (id = %d) in position <%d,%d>" % (self.id, self.x, self.y))
       
    
    # some getter/setter
    def setX(self, x):
        self.x = x
        return x
        
    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y
        return y

    def getY(self):
        return self.y
    
    def setId(self, id):
        self.id = id
        return self.id
    
    def getId(self):
        return self.id
    