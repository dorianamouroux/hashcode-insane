import os.path

class Parser():
    def __init__(self, filename):
        self.filename = filename

        # configuration
        self.rows = 0
        self.columns = 0
        self.drones = 0
        self.deadline = 0
        self.maxDroneLoad = 0
        self.productsType = 0
        self.weights = list()
        self.numberOfWH = 0
        self.warehouses = dict()
        self.numberOfOrders = 0
        self.oders = dict()

        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                self.content = f.read().splitlines()
        else:
            print("%s: File not found" % filename)

        # parse configuration

        # environment
        line = self.content[0].split(' ')
        self.rows = int(line[0])
        self.columns = int(line[1])
        self.drones = int(line[2])
        self.deadline = int(line[3])
        self.maxDroneLoad = int(line[4])

        # number of products
        self.productsType = int(self.content[1])

        # weights of each products
        self.weights = self.content[2].split(' ')

        # number of warehouse
        self.numberOfWH = int(self.content[3])

        # configuration of each warehouses
        for i in range(0, self.numberOfWH):
            newWH = list()
            newWH.append(self.content[4 + i].split(' '))
            newWH.append(self.content[4 + i + 1].split(' '))
            self.warehouses[i] = newWH

        # number of orders
        self.numberOfOrders = int(self.content[5])

        # configuration of each orders
        for i in range(0, self.numberOfOrders):
            newOrder = list()
            newOrder.append(self.content[6 + i].split(' '))
            newOrder.append(int(self.content[6 + i + 1]))
            newOrder.append(self.content[6 + i + 2].split(' '))

    def display(self):
        print(self.rows, self.columns, self.drones, self.deadline, self.maxDroneLoad)
        print(self.productsType)
        print(self.weights)
        print(self.warehouses)

    # Getters

    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns

    def getDrones(self):
        return self.drones

    def getDeadline(self):
        return self.deadline

    def getMaxDroneLoad(self):
        return self.maxDroneLoad

    def getProductType(self):
        return self.productsType

    def getWeights(self):
        return self.weights

    def getNumberOfWarhouses(self):
        return self.numberOfWH

    def getWarehouses(self):
        return self.warehouses

    def getOrders(self):
        return self.orders
