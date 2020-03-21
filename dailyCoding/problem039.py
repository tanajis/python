
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Dropbox.
# Conway's Game of Life takes place on an infinite two-dimensional board of square cells. 
# Each cell is either dead or alive, and at each tick, the following rules apply:
# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
# Implement Conway's Game of Life. 
# It should be able to be initialized with a starting list of live cell coordinates 
# and the number of steps it should run for. Once initialized, 
# it should print out the board state at each step. 
# Since it's an infinite board, print out only the relevant coordinates, 
# i.e. from the top-leftmost live cell to bottom-rightmost live cell.
# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

# Input : ..........
#         ...**.....
#         ....*.....
#         ..........
#         ..........
# Output: ..........
#         ...**.....
#         ...**.....
#         ..........
#         ..........
#         ..........

# Input : ..........
#         ...**.....
#         ....*.....
#         ..........
#         ..........
#         ...**.....
#         ..**......
#         .....*....
#         ....*.....
#         ..........
# Output: ..........
#         ...**.....
#         ...**.....
#         ..........
#         ..........
#         ..***.....
#         ..**......
#         ...**.....
#         ..........
#         ..........
#=============================================================================================
#!/usr/bin/env python
#title           :problem039.py
#description     :DailyCoding #39   Medium - Conway's Game of Life
#author          :Tanaji Sutar
#date            :2020-Mar-21
#python_version  :2.7/3
#ref             :
#============================================================================================

from __future__ import print_function
from copy import deepcopy


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print("*",end=" ")
            
        print("\n")

def getAlivenaiboursCount(pos,input_board):

    cnt = 0
    x,y = pos[0] , pos[1]

    #check up
    up_x,up_y = x-1 , y
    if up_x >=0:
        if input_board[up_x][up_y] == 1:
            cnt += 1

    #check down
    down_x,down_y = x+1 , y
    if down_x < MAX_ROWS:
        if input_board[down_x][down_y] == 1:
            cnt += 1

    #check left side
    left_x,left_y = x , y-1
    if left_y >= 0 :
        if input_board[left_x][left_y] == 1:
            cnt += 1

    #check right side
    right_x,right_y = x , y+1
    if right_y < MAX_COLS :
        if input_board[right_x][right_y] == 1:
            cnt += 1
    
    #----diagonally adjecent positions

    #North East
    ne_x,ne_y = x-1 , y+1
    if ne_x >=0  and ne_y < MAX_COLS :
        if input_board[ne_x][ne_y] == 1:
            cnt += 1

    #South East
    se_x,se_y = x+1 , y+1
    if se_x < MAX_ROWS and se_y < MAX_COLS:
        if input_board[se_x][se_y] == 1:
            cnt += 1
    
    #North West
    nw_x,nw_y = x-1 , y-1
    if nw_x >=0 and nw_y >=0  :
        if input_board[nw_x][nw_y] == 1:
            cnt += 1

    #South West
    sw_x,sw_y = x+1 , y-1
    if sw_x < MAX_ROWS and sw_y >= 0  :
        if input_board[sw_x][sw_y] == 1:
            cnt += 1


    return cnt


def nextGeneration(input_board):

    print('---Input board---')
    printBoard(input_board)

    output_board =deepcopy(input_board) 

    #get Dimensions
    global MAX_ROWS
    global MAX_COLS
    MAX_ROWS = len(input_board)
    MAX_COLS = len(input_board[0])

    #print(getAlivenaiboursCount([9,7],input_board))

    for i in range(MAX_ROWS):
        for j in range(MAX_COLS):
            #get alive neighbours count
            alive_neigbours_cnt = getAlivenaiboursCount([i,j],input_board)
            
            
            if input_board[i][j] == 1:
                #print(i,j,alive_neigbours_cnt)
                
                #---for all live cells-------------------------

                # Any live cell with less than two live neighbours dies.
                if alive_neigbours_cnt < 2:
                    output_board[i][j] = 0


                # Any live cell with two or three live neighbours remains living.
                if alive_neigbours_cnt == 2 or alive_neigbours_cnt == 3 :
                    output_board[i][j] = 1

                # Any live cell with more than three live neighbours dies.
                if alive_neigbours_cnt > 3 :
                    output_board[i][j] = 0
            
            else:
                #---for all dead cells---
                # Any dead cell with exactly three live neighbours becomes a live cell.
                if alive_neigbours_cnt == 3 :
                    output_board[i][j] = 1

    print('---output Baord---')
    printBoard(output_board)

if __name__ == "__main__":
      
    input_board = [ 
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], 
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]

    nextGeneration(input_board)
