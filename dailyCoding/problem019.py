# This problem was asked by Facebook.
# A builder is looking to build a row of N houses that can be of K different colors.
#  He has a goal of minimizing cost while ensuring that no two
#  neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column 
# represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

#----------------------------------------------------------------------------------

#N= number of houses Ex.5 (Rows)
#K=number of colours Ex.take 3 (Coulumns)
#No nighbours should have same colours. SO we will need atleast 2 different colour.

#<--columns 3 colurs---
# #   0    1     2
# 0   50   70   22
# 1   43   32   12 
# 2   21   86   33 
# 3   87   12   98
# 4   54   59   21

#Given is the row of houses
#h1 h2 h3 h4 h5
#c1,c2,c3

#=============================================================================================
#!/usr/bin/env python
#title           :problem019.py
#description     :Daily coding #Medium
#author          :Tanaji Sutar
#date            :2020-Mar-19
#python_version  :2.7/3
#ref             :
#============================================================================================

#----Backtracking-----------------------------------
#First Get all possible combination using Backtracking(push-->check-->pop)
#Then find cost of every combination and return minimum cost 


import copy

def getPosibleCombination(stk,col,allCombos):
    if len(stk) == 5:
        #all are coloured
        return True

    if not stk:
        stk.append(col[0])
    for c in col:
        #colour should not be same as previous house's colur
        if stk and c != stk[-1]:
            stk.append(c)
            res = getPosibleCombination(stk,col,allCombos)
            if res == True:
                allCombos.append(copy.deepcopy(stk))
            stk.pop()

def findMinimumCost(n,k,costArray):
    stk = []
    col = range(k)
    global allCombos
    allCombos = []
    getPosibleCombination(stk,col,allCombos)
    #print(allCombos)

    #find minimum cost now
    minCost = None
    minCostCombo = None
    for solution in allCombos:
        cost = 0
        for i in range(n):
            j = solution[i]
            cost = cost + costArray[i][j]
        
        if minCost is None:
            minCost = cost
            minCostCombo = solution
        elif cost < minCost:
            minCost = cost
            minCostCombo = solution

    return minCost,minCostCombo
if __name__ == "__main__":
    n = 5
    k = 3
    costArray = [ 
        [50,70,22],
        [43,32,12],
        [21,86,33],
        [87,12,98],
        [54,59,21] ]

    minCost,minCostCombo = findMinimumCost(n,k,costArray)
    print('minCost: %i with combination:%r'%(minCost,minCostCombo))
    







