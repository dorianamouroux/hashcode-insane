# insane team

from insane.WareHouse import WareHouse

class Core:
    
    def __init__(self, x, y, nbTurn, maxPayload):
        self.x = x
        self.y = y
        self.nbTurn = nbTurn
        self.maxPayload = maxPayload
        self.WHList = []
        
    def addWareHouse(self, posX, posY):
        newWH = WareHouse(posX, posY, len(self.WHList))
        self.WHList.append(newWH)
        return newWH.getId()
    
    def getWareHouse(self, pos):
        return self.WHList[pos]
    
#    def addProductWareHouse(self, idWH, product):
        