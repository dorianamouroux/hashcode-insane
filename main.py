#!/usr/bin/python3

from insane.Core import Core

def main():
    core = Core(100, 100, 5, 50, 500)
    
    core.addProductType(400)
    core.addProductType(200)
    core.addProductType(300)
    
    wareHouseId = core.addWareHouse(20, 4)
    
    core.addProductWareHouse(wareHouseId, 0, 5)
    core.addProductWareHouse(wareHouseId, 1, 1)
    core.addProductWareHouse(wareHouseId, 2, 0)

    core.getWareHouse(0).toString()

    core.addProductType(500)
if __name__ == "__main__":
    main()
