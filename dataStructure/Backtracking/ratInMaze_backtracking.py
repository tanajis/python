#=============================================================================================
#!/usr/bin/env python
#title           :RatInMaze.py (backtracking)
#description     :Rat In maze problem with only two moves(fw and down)
#author          :Tanaji Sutar
#date            :2020-Mar-07
#python_version  :2.7/3  
#============================================================================================

#---------------------------------------------------------------------------------------
# ref :https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
# A Maze is given as N*N binary matrix of blocks where source block is the upper 
# left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., 
# maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can
# move only in two directions: forward and down.
# In the maze matrix, 0 means the block is a dead end and 1 means the block can be used 
# in the path from source to destination. Note that this is a simple version of the
# typical Maze problem. For example, a more complex version can be that the rat can
# move in 4 directions and a more complex version can be with a limited number of moves.

#Ref :https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/

# {1, 0, 0, 0}
# {1, 1, 0, 1}
# {0, 1, 0, 0}
# {1, 1, 1, 1}

#---------------------------------------------------------------------------------------
#start = 00 end 33  Moves : only down and forward
#0 means deadends and 1 means block can be used to walk

#My Approach
#Step 1:if Rat reached at the end, return true
#Step 2:Set Curr at start.Push curr to stack
#Step 3:for node in all posible moves and not visisted already. 
# Repeat step 4 to 6 for each  node
#Step 4:push curr to stack
#Step 5:Perform recursvively for that node uf Rat reaches at the end.
#step 6:If reached at the end print the stack
#Step 7:pop curr from stack


def getAllPossibleNextMoves(pos):
    
    #Rat can move either forward or down only
    x,y = pos[0],pos[1]
    moves  = []
    if x < 3 and (maze[x+1][y] == 1):
        moves.append([x+1,y])
    if y < 3 and maze[x][y+1] == 1:
        moves.append([x,y+1])
    return moves

def ratinMaze(pos,maze,stk):
    #print('call',pos,stk)
    #base eocndition
    if stk:
        #If RAT reached at the end destination, return true
        if stk[-1] == end:
            return True
    
    #If stk is empty means at stating position set curr at start
    #Append start to stack
    if not stk:
        curr =[0,0]
        stk.append(curr)
    else:
        #Set curr to given pos
        curr = pos
    
    #Get all posible moves
    nextMoves = getAllPossibleNextMoves(curr)
    
    #Check if they are already vsisited.If yes remove it(Exclude)
    for move in nextMoves:
        if stk.__contains__(move):
            nextMoves.remove(move)

    if len(move) == 0:
        #RAT cant move anywhenere and not erached at target.return false
        return False
    
    #print('nextMoves',nextMoves)
    for move in nextMoves:

        #push the pos to stk
        stk.append(move)

        #check recursively for pos
        res = ratinMaze(move,maze,stk)
        if res == True:
            #if True print the path
            print(stk)
        
        #pop the pos from stk
        stk.pop()




if __name__ == "__main__":
    
    maze=[[1,0,0,0],
          [1,1,0,1],
          [0,1,0,0],
          [1,1,1,1]]
    
    start = [0,0]
    end   =[3,3]
    stk = []
    pos =start
    ratinMaze(pos,maze,stk)

    #Expected ans 00,10,11,21,31,32,33
