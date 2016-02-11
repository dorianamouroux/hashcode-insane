# insane team

class Product:
    
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight
        
    def getId(self):
        return self.id
    
    def getWeight(self):
        return self.weight
    
    def toString(self):
        print("I am a product (id = %d) and my weight is %d" % (self.id, self.weight))