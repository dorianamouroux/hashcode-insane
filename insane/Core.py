# insane team

from insane.WareHouse import WareHouse
from insane.Product import Product
from insane.Order import Order
from insane.Drone import Drone

class Core:

    def __init__(self, x, y, nbDrone, nbTurn, maxPayload):
        self.x = x
        self.y = y
        self.nbDrone = nbDrone
        self.nbTurn = nbTurn
        self.maxPayload = maxPayload
        self.WHList = []
        self.drone = []
        self.productType = []
        self.orders = []
        self.createDrone(nbDrone)
    
    # drone function
    def createDrone(self, nb):
        i = 0
        for i in range(0, nb):
            newDrone = Drone(len(self.drone))
            self.drone.append(newDrone)
    
    def setPositionDrone(self):
        warehouse = self.getWareHouse(0)
        for drone in self.drone:
            drone.setX(warehouse.getX())
            drone.setY(warehouse.getY())

    # product type function
    def addProductType(self, weight):
        newProduct = Product(len(self.productType), weight)
        self.productType.append(newProduct)
        return newProduct.getId()

    def getProductType(self, pos):
        return self.productType[pos]

    # warehouse functions
    def addWareHouse(self, posX, posY):
        newWH = WareHouse(posX, posY, len(self.WHList), len(self.productType))
        if newWH.getId() == 0:
            self.setPositionDrone()
        self.WHList.append(newWH)
        return newWH.getId()

    def getWareHouse(self, pos):
        return self.WHList[pos]

    def addProductWareHouse(self, idWareHouse, idProduct, quantity):
        self.getWareHouse(idWareHouse).addProduct(idProduct, quantity)

    # order function
    def addOrder(self, posX, posY):
        newOrder = Order(posX, posY, len(self.orders), len(self.productType))
        self.orders.append(newOrder)
        return newOrder.getId()
    
    def getOrder(self, pos):
        return self.orders[pos]
    
    def addItemOrder(self, idOrder, idItem, quantity):
        product = self.getProductType(idItem)
        self.getOrder(idOrder).addItem(product, quantity)
        
    # some logging function
    
    def printAll(self):
        self.printAllType()
        self.printAllWareHouse()
        self.printAllOrder()
        self.printAllDrone()
    
    def printer(self, word, toRead):
        i = 0
        print("Print all ", word, " : \n")
        for item in toRead:
            if i == 1:
                print("-----")
            item.toString()
            i = 1
        print("\n")
        
    def printAllWareHouse(self):
        self.printer("WareHouse", self.WHList)

    def printAllType(self):
        self.printer("Product Type", self.productType)
    
    def printAllOrder(self):
        self.printer("Order", self.orders)
        
    def printAllDrone(self):
        self.printer("Drone", self.drone)
