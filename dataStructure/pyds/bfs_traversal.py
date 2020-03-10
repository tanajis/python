
#=============================================================================================
#!/usr/bin/env python
#title           :bfs_traversal.py
#description     :Breadth First Traversal/search
#author          :Tanaji Sutar
#date            :2020-Mar-10
#python_version  :2.7/3
#============================================================================================


#IMP Note : in dfs , recursion is used but in BFS it is not

# 1.set curr to starting node
# 2.enque curr node to queue
# 3.for all connected directly to curr and not visited yet repeat 4,5,6
# 4.print the node 
# 5.enque to the queue (at end position [-1])
# 6.if all visited,deque the curr (from start position [0])
# 7.repeat from 3 for first elememt at [0]

#in simple words  print-->enqueue at the end-->explore first-->deque first

#Example 1:
# BFS will be :ABCDEFGH (level wise)
# DFS will be :ABEHFCGD (deapth wise)
#
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
# V = [A,B,C,D,E,F,G,H]
# E = ['AB','AC','AD','BE','CF','DG','EH','FH','GH']
# G=  [V,E]
#
#
#Example 2: BF traversal  will  be [A,D,F,B,E,C,G]
#    A-----B-------C
#   / \   /  \    / \
#  /   \ /    \  /   \ 
# D-----F------E------G 
#
#

#IMP Note : in dfs , recursion is used but in BFS it is not

from collections import deque
def bfs_traverse(G):
    V = G[0]
    E = G[1]
    visisted =[]

    #create Queue
    Q = deque()

    #if no node visisted yet, set curr to first node
    if not visisted:
        curr = V[0]
        #add curr to queue
        Q.appendleft(curr)

        #mark it as visisted
        visisted.append(curr)

    #print(Q,visisted)
    #perform until all nodes are visisted
    while len(visisted) < len(V):
        
        #Set curr to last element in Queue
        curr = Q[-1]
        #print('curr',curr,Q,visisted)
        
        #get all the nodes which are not visisted yet and directly connected to curr node
        nodes_to_visit =[]
        for node in V:
            #print(node)
            #if direct connected
            if E.__contains__(node + curr) or E.__contains__(curr+node):
                #if not visited already
                if not visisted.__contains__(node):
                    nodes_to_visit.append(node)

        #print('nodes_to_visit',nodes_to_visit)
        
        #check if there are nodes to be visisted
        if nodes_to_visit:
            for newNode in nodes_to_visit:

                #Add new node to queue at left end
                Q.appendleft(newNode)

                #mark it as visited
                visisted.append(newNode)

                #print('Add to Q',Q,visisted)
        
        #Once all connected to curr are visited, pop up the curr node
        if Q:
            Q.pop()

        #If all nodes are visited exit from the loop and print the answer
        if len(visisted) == len(V):
            break
    
    s =''
    for tmp in visisted:
        s = s + tmp
    return str(s)

    
    



if __name__ == "__main__":

    print('test case 1')

    V = ['A','B','C','D','E','F','G','H']
    E = ['AB','AC','AD','BE','CF','DG','EH','FH','GH']
    G=  [V,E]
    ans = bfs_traverse(G)

    #Ans shoould be ABCDEFGH
    print(ans)

    print('test case 2')

    V = ['A','B','C','D','E','F','G']
    E = ['AB','AD','AF','BF','BC','BE','EC','CG','FE','DF','EG']
    G=  [V,E]

    #ans should be ABDFCEG
    ans = bfs_traverse(G)
    print(ans)

    """
    BFS traversal will be :ABDFCEG

       A-----B-------C
      / \   /  \    / \
     /   \ /    \  /   \ 
    D-----F------E------G 
    
    visit A
    enq A  Q[A]  visisted [A]
    visit D F S enque  Q[A,D,F,B]  visisted [A,D,F,B]
    All connected to A are visited.Exploration of A completed.Deque it from Que
    Q[D,F,B]
    First element in Q is D. Start exploring it
    F is already visited so no node to visit. Deque D from Q
    Q[F,B]
    First element is  F, start Explorating it
    found E add to Q at the end   Q[F,B,E]  mark as visisted [A,D,F,B,E]
    E is explored completely, rempove it
    Q : Q[B,E]
    
    Start Exploring B
    E is already visisted, C not yet hence add C to Q and mark it visisted
    Q =[B,E,C]  visisted = [A,D,F,B,E,C]
    B exploration completed, remove from que Q[E,C] 
    
    Start exploring E
    C is already visisted but G is not.
    add G at the end of Queue Q:[E,C,G] and mark it visited [A,D,F,B,E,C,G]
    Exploration of E completed, remove it from Queue  Q:[C,G]


    Start Exploring C
    B,E,G are already visisted.No need to explore C
    remove C from Queue Q : [G]

    Start Explorating G 
    Nothing to do for G , remove it from Queue
    
    Final output is Visited :[A,D,F,B,E,C,G]
    """
