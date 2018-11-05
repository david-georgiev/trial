# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:33:51 2018

@author: David
"""

class Item():
    def __init__(self, id, description ,value):
        self.id = id
        self.description = description
        self.value = value
        
    def __str__(self):
        return "ID: {}\nDescription: {}\nValue: {}".format(self.id, self.description, self.value)

class Warehouse():
    inventory = []
    capacity = 2000000000
    remaining_capacity = 2000000000

    def add_item(self, item):
        
        self.inventory.append(item)
        self.remaining_capacity -= item.value

    def remove_item(self, item):
        self.inventory.remove(item)
        self.remaining_capacity += item.value

wh_A, wh_B, wh_C, wh_D = Warehouse(), Warehouse(), Warehouse(), Warehouse()

total_capacity = wh_A.capacity + wh_B.capacity + wh_C.capacity + wh_D.capacity
total_remaining_capacity = 0

def update_remaining_capacity():
    global total_remaining_capacity
    total_remaining_capacity = wh_A.remaining_capacity + wh_B.remaining_capacity + wh_C.remaining_capacity + wh_D.remaining_capacity

def add_item(warehouse ,item):
    if item.value > 2000000000:
        print("error")
    if item.value > total_remaining_capacity:
        print("error")
    if item.value < warehouse.remaining_capacity:
        warehouse.add_item(item)
    if item.value > warehouse.remaining_capacity:
        print("ksekinane ta duskola")
    update_remaining_capacity()


def loadfile()
for line in file:
    new_item = Item(line.prwtokmmati, line.deuterokommati, line.tritokommati)
    add_item(wh_A, new_item)
    



def quicksort(l):
    if len(l) <=1:
        return l
    smaller,equal,larger = [],[],[]
    pivot=l[randint(0,len(l)-1)]
    
    for i in l:
        if i <pivot:
            smaller.append(i)
        elif i == pivot:
            equal.append(i)
        else:
            larger.append(i)
        
        return quicksort(smaller)+equal+quicksort(larger)
    
        
