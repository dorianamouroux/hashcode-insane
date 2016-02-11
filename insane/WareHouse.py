# insane team

class WareHouse:
    
    def __init__(self, posX, posY, id, nbProduct):
        self.x = posX
        self.y = posY
        self.id = id
        self.products = [0] * nbProduct
    
    def addProduct(self, product):
        self.products.append(product)
    
    def hasProduct(self, id):
        if self.products[id] > 0:
            return true
        else:
            return false
    
    def addProduct(self, idProduct, quantity):
        self.products[idProduct] = quantity
    
    def toString(self):
        print("I am a warehouse (id = %d) in position <%d,%d>" % (self.id, self.x, self.y))
        print("This is my inventory : ", self.products)
    
    # some getter/setter
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getId(self):
        return self.id
    