# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:51:45 2018

@author: David
"""
mainmenu = ["1:Add a new item ", "2:Move an item", "3:search an item",
            "4:view the inventory of a warehouse", "0: exit the system"]
def menu():
    # display a main menu
    for i in mainmenu:
        print(i)
    # get the choice from the keyboard
    c = input("please choose a number or press any other key to return:")
    if c == '1':
        addNewItem()
    elif c == '2':
        moveItem()
    elif c == '3':
        searchItem()
    elif c == '4':
        displayInventory()
    elif c == '0':
        exit(0)
    else:
        menu()

def loadFile():
    
    global warehouseATV
    global warehouseA
    with open("DADSA Assignment 2018-19 Warehouse A.csv ") as f:
        f.readline()

        csv_reader = csv.reader(f)

        for line in csv_reader:
            print(line)
            warehouseA.append(line)
            warehouseATV = warehouseATV + int(line[2])
menu()
print(warehouseATV)
        
class Warehouse:
    
    items = []
    def __init__(self, name, totalCapacity = 8000000000, currentCapacity = 0):
        self.name = name
        self.capacity = capacity
    def sortItems():
    def addNewItem():
    def moveItem():
    def displayInventory():
        
        itemId = input("Insert item ID")
        
        
class WarehouseA(Warehouse):
    pass

class WarehouseB(Warehouse):
    pass

class WarehouseC(Warehouse):
    pass

class WarehouseD(Warehouse):
    pass

class Item:

    def __init__(self, itemId, description, value):
        self.itemId = itemId
        self.description = description
        self.value = value
    
      