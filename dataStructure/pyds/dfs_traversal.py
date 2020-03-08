

#=============================================================================================
#!/usr/bin/env python
#title           :dfs_traversal.py
#description     :Deapth First Traversal/search
#author          :Tanaji Sutar
#date            :2020-Mar-08
#python_version  :2.7/3
#============================================================================================

#-----My Notes ---------------------
#
#For DFS we always need STACK 
# #push -->process --pop

# 1.set curr to the start vertex.
# 2.print vertex. mark it as visisted and PUSH TO STACK
# 3.for every adjescent but unvisisted node to curr perfrom steps 4 to 7
# 4.set curr = node
# 5.mark it as visisted ,print and PUSH TO STACK 
# 6.call repeat 3 and 4 for 
# 7.If all adjescent are visisted or no any adjescent to curr,pop curr node
#end
#ABEHFCGDCD
#Example
#           A
#         / | \
#        /  |  \
#       B   C   D
#       |   |   |
#       E   F   G
#        \  |  /
#         \ | /
#           H
#
#Start  at A
#DFS will be  A-->B-->E-->H-->F-->C-->G-->D  (ABEHFCGD)
#             A-->B-->E-->H-->G-->D-->F-->C  (ABEHGDFC)
# V = [A,B,C,D,E,F,G,H]
# E = ['AB','AC','AD','BE','CF','DG','EH','FH','GH']
# G=  [V,E]
#---------------------------------------------------------------------------------



def dfs(G):
    V =G[0]
    E =G[1]
    stk = []
    visisted =[]

    res = dfs_traverse(stk,visisted,E,V)
    
    return True

def dfs_traverse(stk,visisted,E:list,V):

    #Base case 
    #if All visisted Return true
    if len(visisted) == len(V):
        return True

    #If not any node visisted yet, set curr to Start node
    if len(visisted) == 0:
        #Starting node
        curr = V[0]
        print(curr ,end= '')
        #push to stack
        stk.append(curr)
        #mark as visited
        visisted.append(curr)

    else:
        curr = stk[-1]
    
    #get all connected and unvisisted nodes
    adj_unvisisted =[]
    for node in V:
        #Check if it is adjescent
        if E.__contains__(node + curr) or E.__contains__(curr+node):
            #if adjescent and not visisted , append
            if not visisted.__contains__(node):
                adj_unvisisted.append(node)

    for node in adj_unvisisted:

        #IMP : Check AGAIN if it is visisted already by previous recursive loop
        #If yes then skip that node
        if (visisted.__contains__(node)):
            continue
        
        #Set Curr to node
        curr = node
        
        #print curr
        print(curr,end= '')
        
        #PUSH to STACK
        stk.append(curr)

        #Mark as visisted
        visisted.append(curr)

        #Recusrivley call fucntion for cuur node
        res = dfs_traverse(stk,visisted,E,V)
        
        #POP the curr node from stack
        stk.pop()


if __name__ == "__main__":
    V = ['A','B','C','D','E','F','G','H']
    E = ['AB','AC','AD','BE','CF','DG','EH','FH','GH']
    G=  [V,E]
    dfs(G)

    #Expected ans ABEHFCGD
