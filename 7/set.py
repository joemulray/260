#!/usr/bin/env python

"""
Joseph Mulray
CS260
HW7: Implimenting Disjoint Sets
2/28/17
"""

class DSS:
    #Class to represent disjoint set system
    def __init__( self, value = None):
        self.value = value
        self.parent = self
        self.height = 0


def Initialize(Values):
    #creates n one element sets given an array of n thing
    return [DSS(element) for element in Values]

def Find(set, value):
    #cycle through list compare elements value to searching value
    isTrue = False

    for element in set:    
        if element.value is value:
            isTrue = True
            foundVal = element

    #is value is not in set values just return None
    if not isTrue:
        return None

    if foundVal.parent is not foundVal:
        parentVal = foundVal.parent.value
        #recall find to get root of parent
        foundVal.parent = Find(set, parentVal)

    #return the parent of the value
    return foundVal.parent


def Merge(set, value1, value2):
    #find the parent roots for the two values
    set1 = Find(set, value1)
    set2 = Find(set, value2)

    #compare highest roots set the lowest root
    #parent to which is bigger, 
    if set1.height > set2.height:
        set2.parent = set1
        set1.height += set2.height

    elif set1.height < set2.height:
        set1.parent = set2
        set2.height += set1.height

    elif set1.height is set2.height:
        #just adding to set1, vice versa with set2 as parent
        set2.parent = set1
        set1.height += 1
    else:
        pass 



