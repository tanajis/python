
def decToBinary(n):
    res = ''
    while(n>=1):
        res = str(n%2) + res  
        n = n/2

    return int(res)


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




Googles guide for all languages:
http://google.github.io/styleguide/
https://realpython.com/python-comments-guide/
https://www.python.org/dev/peps/pep-0257/





#-----------yes to all prompt in shell cammands

yes|rm -R folder1


# oracle client library issue

https://oracle.github.io/odpi/doc/installation.html#windows
https://stackoverflow.com/questions/56119490/cx-oracle-error-dpi-1047-cannot-locate-a-64-bit-oracle-client-library

https://oracle.github.io/odpi/doc/installation.html#windows
Download and copy to c://oracle and add

:
