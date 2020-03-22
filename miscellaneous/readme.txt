

def int2bin(integer, digits):
    #
    #User defined fundtion to get binary representation of given integer
    ######################################################################
    if integer >= 0:
        return bin(integer)[2:].zfill(digits)
    else:
        return bin(2**digits + integer)[2:]
       
       
Ex.combination = int2bin(2,3)
Ex.combination = int2bin(2,3)
Ex.combination = int2bin(2,3)



#create Board 
    # Note if we use [0]*n  or [None]*n  then it makes shollow copies and when we update any one all get updated which is worng
    board = []
    for row in range(n):
        temp = []
        for col in range(n):
            temp.append(0)
        board.append(temp)

[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



In python 2x  print with end doe not work .It works in 3 only
Ex. print(board[i], end=" ")

to get ot work, just import below in 2x
from __future__ import print_function




#----------------HEAP/Priority Queue inbuild python package--------------

import heapq as hq

min_heap = list()
hq.heapify(mylist)

Or 

min_heap = []
hq.heappush(min_heap, 5)
v = hq.heappop(min_heap)

If you want max heap just add -ve sign while read/write from heapq
