# This problem was asked by Facebook.
# You are given an array of non-negative integers that represents a two-dimensional
#  elevation map where each element is unit-width wall and the integer is the height. 
# Suppose it will rain and all spots between two walls get filled up.
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the 
# second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), 
# so we can trap 8 units of water.

#=============================================================================================
#!/usr/bin/env python
#title           :problem030.py
#description     :DailyCoding #030  Medium
#author          :Tanaji Sutar
#date            :2020-Mar-19
#python_version  :2.7/3
#============================================================================================


def getWatertot_water_qty(elevation_array):

    #form matrix
    max_hight = max(elevation_array)
    steps  = len(elevation_array)
    elevation_matrix = []
    
    #Note : This didnt worked as it make copy [[0] * steps] * max_hight
    #And create problem when we update any element

    # Create elevation_matrix
    for i in range(max_hight):
        temp = []
        for j in range(steps):
            temp.append(0)
        elevation_matrix.append(temp)

    # mark 1 if wall
    wallnumber = 0
    for hight in elevation_array:
        step = 0

        #Start from bottom up to hight mark as 1
        while(step < hight):
            #bottom is A[max_hight][wallnumber] go upward
            elevation_matrix[max_hight-step-1][wallnumber] = 1
            step += 1
        
        #Move to next wall(next column)
        wallnumber += 1

    #Now matrix is ready.So calcultae water amout for per row

    tot_water_qty = 0
    for row in range(len(elevation_matrix)):
        #cntFlag is Y if water can be stored
        cntFlag = 'N'
        cnt = 0
        row_water_qty = 0
        #start from left and move towards right
        for pos in range(len(elevation_matrix[row])):
            
            #if wall is found
            if elevation_matrix[row][pos] == 1:
                #is it laft wall
                if cnt == 0:
                    #left wall found so we can start counting
                    cntFlag = 'Y'
                else:
                    #wall is found and it is right side wall.
                    #So add water amount counted to row_water_qty
                    row_water_qty = row_water_qty + cnt
                    
                    #set count to zero
                    cnt = 0
            
            #if water can be stired and flag is Y then add 1 unit
            if elevation_matrix[row][pos] == 0 and cntFlag == 'Y':
                cnt = cnt + 1
        
        #Add the qty for this row to total qty
        tot_water_qty = tot_water_qty + row_water_qty
    
    return tot_water_qty      









    



if __name__ == "__main__":
    elevation_array = [3, 0, 1, 3, 0, 5]
    assert getWatertot_water_qty(elevation_array) == 8
    elevation_array = [2, 1, 2]
    assert getWatertot_water_qty(elevation_array) == 1
