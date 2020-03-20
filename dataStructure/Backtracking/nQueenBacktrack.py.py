
"""

ref :https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/

1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column. 
   Do following for every tried row.
    a) If the queen can be placed safely in this row 
       then mark this [row, column] as part of the 
       solution and recursively check if placing
       queen here leads to a solution.
    b) If placing the queen in [row, column] leads to
       a solution then return true.
    c) If placing queen doesn't lead to a solution then
       unmark this [row, column] (Backtrack) and go to 
       step (a) to try other rows.
3) If all rows have been tried and nothing worked,
   return false to trigger backtracking.

for 4 Queen answer should be below
option1
 0  0  1  0 
 1  0  0  0 
 0  0  0  1 
 0  1  0  0 

option2
 0  1  0  0 
 0  0  0  1 
 1  0  0  0 
 0  0  1  0 

"""

#=============================================================================================
#!/usr/bin/env python
#title           :nqueen_backtrac.py
#description     :4 Queen problem using backtracking
#author          :Tanaji Sutar
#date            :2020-Mar-05
#python_version  :2.7/3  
#============================================================================================

from copy import deepcopy

def isUnderAttack(i,j):
    #under attack if same row or same column or same diagonal

    #Column and rows
    for k in range(n):
        if board[i][k]==1 or board[k][j]==1:
            return True
    
    #check diagnonal
    for k in range(n):
        for l in range(n):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    
    return False


def nQueen(n,board):
    #print('call',n,board)
    if n == 0:
        #All Queens are successfully placed.Show the board
        #print(board)
        temp = deepcopy(board)
        
        #Avoid Duplicate output
        if not final_output.__contains__(temp):
            final_output.append(temp)
        
        #clear board
        for m in range(4):
            for n in range(4):
                board[m][n] = 0
        #print('hi',board)
        return True
    
    #for every row
    for i in range(boardsize):
        #for every column
        for j in range(boardsize):
            #check if place (i,j) is empty and not under attach
            if board[i][j] !=1 and not(isUnderAttack(i,j)):
                #condition satisfied,hence put nth queen there
                #print('putting {} at'.format(n),i,j)
                board[i][j] = 1
                #Now check  if REMAINING ALL Queen can be placed recursively.
                if nQueen(n-1,board) == True:
                    #print('Done' ,i,j,n)
                    board[i][j] = 0
                    #if n is 4 then only try next position else just exist from child loop
                    #by returning True
                    if n != 4:
                        return True
                    continue
                else:
                    board[i][j] = 0

                    #if n is 4 then only try next position else just exist from child loop
                    #by returning True
                    if n != 4:
                        return False
                    continue
    return False

if __name__ == "__main__":
    n=4
    boardsize = deepcopy(n)
    board=[[0] *boardsize for _ in range(boardsize)]
    cnt=0
    final_output =[]
    #print(board)
    
    nQueen(4,board)
    print(final_output)
