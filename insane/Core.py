# insane team

class Core:
    
    def __init__(self, x, y, nbTurn, maxPayload):
        self.x = x
        self.y = y
        self.nbTurn = nbTurn
        self.maxPayload = maxPayload
        self.WHList = []
        
    def addWareHouse(self, posX, posY):
        newWH = new WareHouse(posX, posY)
        self.WHList.append(newWH)
    
    def getWareHouse(self, pos):
        return self.WHList[pos]