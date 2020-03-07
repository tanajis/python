#=============================================================================================
#!/usr/bin/env python
#title           :m_colouring_backtracking.py
#description     :M colours map colouring #Backtracking
#author          :Tanaji Sutar
#date            :2020-Mar-07
#python_version  :2.7/3  
#============================================================================================


#---------------------------------------------------------------------------------------------------------------------------
# #https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/
# Given an undirected graph and a number m, determine if the graph can be colored 
# with at most m colors such that no two adjacent vertices of the graph are colored with 
# the same color. Here coloring of a graph means the assignment of colors to all vertices.
# Input:
# 1) A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is 
# adjacency matrix representation of the graph. A value graph[i][j] is 1 if there is a 
# direct edge from i to j, otherwise graph[i][j] is 0.
# 2) An integer m which is the maximum number of colors that can be used.

# Output:
# An array color[V] that should have numbers from 1 to m. color[i] should represent the 
# color assigned to the ith vertex. The code should also return false if the graph cannot be colored with m colors.
#---------------------------------------------------------------------------------------------------------------------------

#My Notes:
# Input graph is as below
#  A--B 
#  |\/
#  |/\  
#  C--D
#
# we have given 3 colours(1,2,3)  only B and D are connected
# E  =[AB,AC,AD,BC]  so A,B,C are adjescent to each other and can not have same colour
# B and D are not adjecsent and can have same colour
# So A :1 B:2 C:3  D:2 --same colur to only B and D as they are not adjescent
# I am taking Graph represetation as G={V,E}
# V =[A,B,C,D] and E =['AB','AC','AD','CD']
# 
# Output should be 1 2 3 2
#
#
#----My aproach (backtracking)-------
#
#Step 1:if All vertex coloured, return true
#Step 2:Set Curr at start.
#       get its colour (initially 1st vertex =1st colour )
#       PUSH curr to stack
#Step 3:for node in all connected vertex to curr and not visisted already. 
#Repeat step 4 to 6 for each  node
#Step 4:Get the colour ,Aplly & PUSH node to stack
#Step 5:Perform recursvively for that node if we can apply colours to all nodes.
#step 6:If reached at the end print the stack
#Step 7:POP node from stack
#--------------------------------------------------------------------------------------
from copy import deepcopy

def m_colour(G,m):
    """
    This is helping function, which calls actual function and refine and print output.
    """
    V = G[0]
    E = G[1]
    coloured_stk = []
    colours = []
    for c in range(m):
        colours.append(c)
    
    c = 0
    output = []
    applyColour(coloured_stk,c,output)
    
    #now output may contai duplicate values

    output2 = []
    for res in output:
        #Sort by name of vertex
        res = sorted(res , key =lambda x:x[0])
        if not (output2.__contains__(res)):
            output2.append(res)

    #print the result    
    for ans in output2:
        for c in ans:
            print(c[1],end=' ')
        print('\n')

def getColour(curr,coloured_stk):
    """
    This is main function which returns valid colour for given vertex.
    Start from 1 to m, return c if 
        c is not used  OR 
        c is already used but not adjucent
    """
    for c in range(1,m+1):
        #c from 1 to m
        flg ='Y'
        #if already applied colour to some nodes
        if coloured_stk:
            for i in coloured_stk:
                node =i[0]
                #if c present in coloured_stk
                if c == i[1]:
                    #Already used
                    #if adjuscent, we cant use c
                    if E.__contains__(curr+node) or E.__contains__(node+curr):
                        #we cant use c as already applied to an adjescent vertex
                        #Break and check for next value of c
                        flg = 'N'
                        break
    
                    else:
                        ##we can use c even of it is already applied as it 
                        # is not an adjescent vertex
                        return c
        if flg =='Y':
            return c
        else:
            continue

def applyColour(coloured_stk,c,output):
    #print('call',coloured_stk,c)

    #base condition
    #if all coloured return True
    if len(coloured_stk) == len(V):
        return True
    
    if len(coloured_stk) == 0:
        #First vertex
        curr = V[0]
        c = 1
        coloured_stk.append([curr,c])
    else:
        curr = coloured_stk[-1][0]
    #Get all vertex which are connected to curr vertex and are not coloured yet
    all_connct_no_colr = []
    temp = [k[0] for k in coloured_stk]
    #print('temp',temp)
    for v in V:
        #If connected
        if E.__contains__(curr+v) or E.__contains__(v+curr):
            #if not coloured yet
            if not(temp.__contains__(v)):
                all_connct_no_colr.append(v)
    
    #print('cur',curr,'all_connct_no_colr:',all_connct_no_colr)
    for nextv in all_connct_no_colr:
        
        #Apply colour to the node
        #Push that node to stack

        c = getColour(nextv,coloured_stk)

        coloured_stk.append([nextv[0],c])

        #Check recursively to that node

        res = applyColour(coloured_stk,c,output)

        if res == True:
            output.append(deepcopy(coloured_stk))
        coloured_stk.pop()

if __name__ == "__main__":
    
    V = ['A','B','C','D']
    E = ['AB','AC','AD','CD','BC']
    G =[V,E]
    m = 3

    m_colour(G,m)

    #Output should be 1 2 3 2

    
