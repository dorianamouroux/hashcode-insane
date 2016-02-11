# insane team

class Order:

    def __init__(self, posX, posY, id, nbItem):
        self.x = posX
        self.y = posY
        self.id = id
        self.weight = 0
        self.items = [0] * nbItem

    def addItem(self, product, quantity):
        self.items[product.getId()] = quantity
        self.weight += (quantity * product.getWeight())

    def getId(self):
        return self.id

    def getWeight(self):
        return self.weight

    def getX(self):
        return (self.x)

    def getY(self):
        return (self.y)

    def toString(self):
        print("I am an Order (id=%d) and my list is " % self.id, self.items, "\nmy total weight is %d" % self.weight)
