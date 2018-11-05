# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:54:22 2018

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
        viewInventory()
    elif c == '0':
        exit(0)
    else:
        menu()
        
def viewInventory():
    c = input("choose the warehouse that you want ro view or press any other key to go back to main menu")
    
    if c == 'A':
        print(WarehouseA)
    elif c == 'B':
        print(WarehouseB)
    elif c == 'C':
        print(WarehouseC)
    elif c == 'D':
        print(WarehouseD)
    else:
        menu()
        
        