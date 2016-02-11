# insane team

from insane.WareHouse import WareHouse
from insane.Product import Product

class Core:

    def __init__(self, x, y, nbDrone, nbTurn, maxPayload):
        self.x = x
        self.y = y
        self.nbDrone = nbDrone
        self.nbTurn = nbTurn
        self.maxPayload = maxPayload
        self.WHList = []
        self.productType = []

    def addWareHouse(self, posX, posY):
        newWH = WareHouse(posX, posY, len(self.WHList), len(self.productType))
        self.WHList.append(newWH)
        return newWH.getId()

    def getWareHouse(self, pos):
        return self.WHList[pos]

    def addProductType(self, weight):
        newProduct = Product(len(self.productType), weight)
        self.productType.append(newProduct)
        return newProduct.getId()

    def addProductWareHouse(self, idWareHouse, idProduct, quantity):
        self.getWareHouse(idWareHouse).addProduct(idProduct, quantity)
