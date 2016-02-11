#!/usr/bin/python3

from insane.Core import Core

def main():
    core = Core(100, 100, 50, 500)
    
    print(core.addWareHouse(20, 4))
    print(core.addWareHouse(20, 4))
    print(core.addWareHouse(20, 4))
    # write your main here
    
    core.getWareHouse(2).toString()

if __name__ == "__main__":
    main()
