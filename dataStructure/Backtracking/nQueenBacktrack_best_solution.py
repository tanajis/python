
#Hard
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Microsoft.
# You have an N by N board. Write a function that, given N, 
# returns the number of possible arrangements of the board where N queens
# can be placed on the board without threatening each other,
# i.e. no two queens share the same row, column, or diagonal.

#=============================================================================================
#!/usr/bin/env python
#title           :NQueenBacktracinkg.py
#description     :DailyCoding #38   HARD - backtraking 
#author          :Tanaji Sutar
#date            :2020-Mar-21
#python_version  :2.7/3
#ref             :
#============================================================================================

# This is an example of backtracking
# push ->check -->pop
#
#IMP : This is without creating the board matrix
#For solution with board matrix check backtracking folder
import copy

def NQueens(n):

    global allPossibleSolutions
    global N 
    N = copy.deepcopy(n)
    
    allPossibleSolutions =[]
    stk = []

    NQueensHelper(n,stk)

    #Sort 
    temp = []
    for sol in allPossibleSolutions:
        sol =sorted(sol)
        if not temp.__contains__(sol):
            temp.append(sol)

    return temp

def isSafe(pos,stk):

    #if same column
    for Q in stk:
        #print(Q,pos)
        #same column or same row
        if Q[0] == pos[0] or Q[1] == pos[1]:
            #print('same diagonal')
            return False
    
    #diagonal 
    for step in range(N):
       
        # increase x , decrease y
        x,y = pos[0],pos[1]
        while(x < N and y >=0 ):
            #print([x,y],stk)
            if stk.__contains__([x,y]):
                return False
            x = x + 1
            y = y - 1

        # decrease x , increase y
        x,y = pos[0],pos[1]
        while(y < N and x >=0 ):
            if stk.__contains__([x,y]):
                return False
            x = x - 1
            y = y + 1

        # decrease x , decrease y
        x,y = pos[0],pos[1]
        while(y >=0 and x >=0 ):
            if stk.__contains__([x,y]):
                return False
            x = x - 1
            y = y - 1
        
        # increase x , increase y
        x,y = pos[0],pos[1]
        while(y < N and x < N ):
            if stk.__contains__([x,y]):
                return False
            x = x + 1
            y = y + 1

    return True


def NQueensHelper(n,stk):

    if n == 0 :
        return True

    #Try all rows and columns

    for i in range(N):
        for j in range(N):
            
            # If puting Queen is safe then only put it
            if isSafe([i,j],stk):
                
                #PUSH to Stack  (backtracking)
                stk.append([i,j])
                
                #Check (backtracking)
                res = NQueensHelper(n-1,stk) 

                if res == True:
                    #Append to final output Array
                    #Note : used Deepcopy as in python variable is just reference and value may change later
                    allPossibleSolutions.append(copy.deepcopy(stk))
                
                #pop from stack (backtracking)
                stk.pop()

if __name__ == "__main__":
    n = 4
    print(NQueens(n))

    assert NQueens(n) == [[[0, 1], [1, 3], [2, 0], [3, 2]], [[0, 2], [1, 0], [2, 3], [3, 1]]]
    





