#!/usr/bin/python3

from insane.Parser import Parser
from insane.Core import Core

def main():
    parser = Parser("sample/busy_day.in")
    parser.display()

    # create the environment
    core = Core(parser.getRows(), parser.getColumns(), parser.getDrones(), parser.getDeadline(), parser.getMaxDroneLoad())

    # create the products type
    weights = parser.getWeights()
    for weight in weights:
        core.addProductType(weight)

    # create warehouses with products
    warehouses = parser.getWarehouses()
    for id, warehouse in warehouses.items():
        wareHouseId = core.addWareHouse(warehouse[0][0], warehouse[0][1])
        i = 0
        for product in warehouse[1]:
            core.addProductWareHouse(warehouse, i, product)

    orders = parser.getOrders()
    for order in orders:
        orderId = core.addOrder(order[0][0], order[0][1])
        i = 0
        for product in order[2]:
            core.addItemOrder(orderId, product, 1)

if __name__ == "__main__":
    main()
