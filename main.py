#!/usr/bin/python3

from insane.Parser import Parser
from insane.Core import Core

def main():
    parser = Parser("sample/little.in")
    parser.display()

    # create the environment
    core = Core(parser.getRows(), parser.getColumns(), parser.getDrones(), parser.getDeadline(), parser.getMaxDroneLoad())

    # create the products type
    weights = parser.getWeights()
    for weight in weights:
        core.addProductType(int(weight))

    # create warehouses with products
    warehouses = parser.getWarehouses()
    for id, warehouse in warehouses.items():
        wareHouseId = core.addWareHouse(int(warehouse[0][0]), int(warehouse[0][1]))
        i = 0
        for product in warehouse[1]:
            core.addProductWareHouse(wareHouseId, i, product)
            i += 1

    orders = parser.getOrders()
    for id, order in orders.items():
        orderId = core.addOrder(order[0][0], order[0][1])
        for product in order[2]:
            core.addItemOrder(orderId, int(product), 1)

    core.printAll()

if __name__ == "__main__":
    main()
