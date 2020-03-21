##############################################################################
# This problem was asked by Google.
# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. 
# You can only swap elements of the array.
# Do this in linear time and in-place.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
#=============================================================================================
#!/usr/bin/env python
#title           :problem035.py
#description     :DailyCoding #35   HARD
#author          :Tanaji Sutar
#date            :2020-Mar-21
#python_version  :2.7/3
#ref             :
#============================================================================================

#Check https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
#Thius is also know as Dutch National Flag Problem
#http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/


#------------------------------------------------------
#---dutch national flag problem algorithm
##------------------------------------------------------

from __future__ import print_function
from copy import deepcopy


def segregate(input_array):

    """
    This is standerd approach using Dutch National Flag Problem
    """
    #take three variables
    #represent R
    low = 0 
    #represent G
    mid = 0 
    #represent B
    high = len(input_array) - 1 

    while(mid <= high):

        if input_array[mid] == 'R':
            ##element at mid is B, move to high, move it to low by swaping
            input_array[mid],input_array[low] = input_array[low],input_array[mid]
            mid = mid + 1
            low = low + 1

        elif input_array[mid] == 'G':
            #element at mid is G then ok ,move to next mid
            mid = mid + 1
        
        elif input_array[mid] == 'B':
            #element at mid is B, move to high by swaping
            input_array[mid],input_array[high] = input_array[high],input_array[mid]
            high = high - 1

    
    return input_array





def segregate2(input_array):
    """
    This is approach designed by me

    """

    map = [0,0,0] #counst of R,G,B

    for c in input_array:
        if c == 'R':
            map[0] = map[0] + 1

        elif c == 'G':
            map[1] = map[1] + 1
        
        elif c == 'B':
            map[2] = map[2] + 1

    output = ['R']*map[0]  +['G']*map[1] + ['B']*map[2]

    return output


if __name__ == "__main__":
      
    input_array = ['G', 'B', 'R', 'R', 'B', 'R', 'G']

    assert segregate(input_array) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']

    print(segregate(input_array))
