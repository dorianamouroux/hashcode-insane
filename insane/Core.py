# insane team

from insane.WareHouse import WareHouse
from insane.Product import Product
from insane.Order import Order

class Core:

    def __init__(self, x, y, nbDrone, nbTurn, maxPayload):
        self.x = x
        self.y = y
        self.nbDrone = nbDrone
        self.nbTurn = nbTurn
        self.maxPayload = maxPayload
        self.WHList = []
        self.productType = []
<<<<<<< HEAD

=======
        self.orders = []
                
    # product type function
    def addProductType(self, weight):
        newProduct = Product(len(self.productType), weight)
        self.productType.append(newProduct)
        return newProduct.getId()
    
    def getProductType(self, pos):
        return self.productType[pos]

    # warehouse functions
>>>>>>> 7fecf20bf149a0bc99973e8d41ec1256b0d9cb90
    def addWareHouse(self, posX, posY):
        newWH = WareHouse(posX, posY, len(self.WHList), len(self.productType))
        self.WHList.append(newWH)
        return newWH.getId()

    def getWareHouse(self, pos):
        return self.WHList[pos]
<<<<<<< HEAD

    def addProductType(self, weight):
        newProduct = Product(len(self.productType), weight)
        self.productType.append(newProduct)
        return newProduct.getId()

    def addProductWareHouse(self, idWareHouse, idProduct, quantity):
        self.getWareHouse(idWareHouse).addProduct(idProduct, quantity)
=======
   
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
>>>>>>> 7fecf20bf149a0bc99973e8d41ec1256b0d9cb90
