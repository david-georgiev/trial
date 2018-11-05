from random import randint
import csv

#import math
#import copy


mainmenu = ["1:Add a new item ", "2:Move an item", "3:search an item",
            "4:view the inventory of a warehouse", "0: exit the system"]

warehouseA = []
warehouseATV = 0



def addNewItem():
    
    global warehouseA
    global warehouseATV
    loadFile()
    itemId = input("Please give the ID")
    description = input("Please give the name or description:")
    value = input("Please give the value")
    warehouse = input("Please give the warehouse name")

    if warehouse == 'A':
        
       warehouseA.append([itemId, description, value])
      #  an oxi kanw kati allo
    warehouseATV += int(value)
    
    for i in warehouseA:
        print(i)
        
def menu():

    # display a main menu
    for i in mainmenu:
        print(i)

    # get the choice from the keyboard
    c = input("please choose a number or press any other key to return:")
    if c == '1':
        addNewItem()
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
        #Itterate throuht the file
        for line in csv_reader:
            #print(line)
            warehouseA.append(line)
            warehouseATV = warehouseATV + int(line[2])

menu()

print("TOTAL VALUE OF WAREHOUSEA IS " , warehouseATV)
print(warehouseA)
#gui beggining
#from tkinter import *
#root = Tk()
#thelabel = Label(root, text="WELCOME")
#theLabel.pack()
#root.mainloop()