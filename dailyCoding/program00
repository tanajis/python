# This problem was asked by Google.
# You are given an M by N matrix consisting of booleans that represents a board. 
# Each True boolean represents a wall. Each False boolean represents a tile 
# you can walk on.
# Given this matrix, a start coordinate, and an end coordinate, return 
# the minimum number of steps required to reach the end coordinate from the start.
#  If there is no possible path, then return null. You can move up, left, down, and right.
#  You cannot move through walls. 
# You cannot wrap around the edges of the board.
# For example, given the following board:

# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), 
# the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) 
# because there is a wall everywhere else on the second row.

#=============================================================================================
#!/usr/bin/env python
#title           :problem023.py
#description     :Minimum Edit Distance between two co-ordinate  #DailyCoding #Easy #DP
#author          :Tanaji Sutar
#date            :2020-Mar-01
#python_version  :2.7/3  
#Note            : 
#============================================================================================

# IMP NOTE  : To solve this we needed deepcopy of cashe each time
import sys
from copy import deepcopy
sysmax = sys.maxsize

def f1(Arr,x1,y1,x2,y2,d,cashe):
    new_cache = deepcopy(cashe)
    if new_cache[x1][y1] == 1:
        return sys.maxsize
    else:
        new_cache[x1][y1] = 1

    #print('call',x1,y1,d)
    #base case
    if x1 == x2 and y1 == y2:
        #reahced at the target
        new_cache[x1][y1] = 1
        #print('reached')
        return d
    elif x1 > 3 or y1 >3 or x1 < 0 or y1 < 0 or cashe[x1][y1] == 1:
        return sys.maxsize
        
    #check if we can move to the left
    res1 = sys.maxsize
    if y1 > 0 and Arr[x1][y1-1] == 'f':
        res1 = f1(Arr,x1,y1-1,x2,y2,d+1,new_cache)

    #check if we can move to the right
    res2 = sys.maxsize
    if y1 < 3 and Arr[x1][y1+1] == 'f':
        res2 = f1(Arr,x1,y1+1,x2,y2,d+1,new_cache)

    #check if we can move to the upword
    res3 = sys.maxsize
    if x1 > 0 and Arr[x1-1][y1] == 'f':
        res3 = f1(Arr,x1-1,y1,x2,y2,d+1,new_cache)

    #check if we can move to the downword
    res4 =sys.maxsize
    if x1 < 3 and Arr[x1+1][y1] == 'f':
        res4 = f1(Arr,x1+1,y1,x2,y2,d+1,new_cache)

    #print('res',res1,res2,res3,res4)
    return min(res1,res2,res3,res4)


if __name__ == "__main__":
    
    Arr = [['f','f','f','f'],
            ['t','t','f','t'],
            ['f','f','f','f'],
            ['f','f','f','f']]

    cashe =   [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
    startx,starty =3,0
    endx,endy =0,0
    distance = 0
    ans = f1(Arr,startx,starty,endx,endy,distance,cashe)

    print('ans',ans)
