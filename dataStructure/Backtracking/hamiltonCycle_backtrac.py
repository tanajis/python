#=============================================================================================
#!/usr/bin/env python
#title           :hamiltonian_cycle_backtrack.py
#description     :This is best example of backtracking
#author          :Tanaji Sutar
#date            :2020-Amr-03
#python_version  :2.7/3  
#problem         :Gievn a graphh return all possible hamiltonian cycles
#============================================================================================

#Notes :
#Hamiltonian Cycle

#All points must be covered and return to starting point
#Should not have duplicate:same cycle ,just starting & ending pooint different is not allowed
#Cant visit any intermediate vertex 2 times
#If graph has articulation point -->No hamilton cycle exist(It dont satisy 3rd condition)
#We need print all possible soltions -->back tracking

#Backtracking work exact same as Deapth first search/traversal (DFS)
#we need stack here

#Step 1: If all node visisted, check if last and first node connected.
#        If Yes then return TRUE else return False
#Step 2: set current to start node, push it to stack
#Step 3: for all nodes directly connected to curr & not visisted yet:
#        push it to stack
#        res1 = recusrively call step 3 for it
#        if res1 is true -->print the path
#        pop it from stack
#





def getConnectedNodes(node):
    allConnectedNodes =[]
    for toNode in V:
        if E.__contains__(node+toNode) or E.__contains__(toNode+node):
            allConnectedNodes.append(toNode)
    
    return allConnectedNodes


def hamiltonianCycle(visited):
    
    #If all visisted
    if len(visited) == tot_nodes:
        if E.__contains__(visited[-1]+visited[0]) or E.__contains__(visited[0]+visited[-1]) :
            #all visisted and last node has way to go to first node.Solution Achieved
            return True
        else:
            #all visisted and last node has DO NOT have a way to go to first node
            #return false here
            return False
    

    #if  all not visisted visit as below

    if len(visited) == 0:
        #point curr to first element in vertex list.(Starting Node)
        curr = V[0]
        visited.append(curr)
    else:
        #point curr to last element in the visited
        curr = visited[-1]
    

    #Get all connected to curr node
    allConneted = getConnectedNodes(curr)
    
    #select only unvisisted nodes from all connected to curr node
    unvisited =[]
    for k in allConneted:
        if not(visited.__contains__(k)):
            #Remove already visisted
            unvisited.append(k)
    
    #IMP : above step will exclude already visisted nodes,So articulation point condition will be 
    #satisfied automatically here


    for node in unvisited:
        #push the node to the visited stack
        visited.append(node)
    
        #call recursively for that node
        res = hamiltonianCycle(visited)
        
        if res == True:
            #If condition is satisfed, print the path
            print('path:',visited)

        #if all connected nodes of this node are visited then pop up this node
        visited.remove(node)

if __name__ == "__main__":
    
    
    V = ['A','B','C','D','E']
    E = ['AB','AD','BD','BC','DC','DE','EC'] 
    G = [V,E]

    visited =[]
    tot_nodes = len(V)
    hamiltonianCycle(visited)

    """
    A----D---E
    |  / |  /
    | /  | /
    B----C
    
    possible hamiltonian cycles are ABCED  and ADECB

    """
