
#Hamiltonian Cycle

#1.All points must be covered and return to starting point
#2.Should not have duplicate:same cycle ,just starting & ending pooint different is not allowed
#3.Cant visit any intermediate vertex 2 times
#4.If graph has articulation point -->No hamilton cycle exist(It dont satisy 3rd condition)
#5.We need print all possible soltions -->back tracking


#1.go to start node
#2.for all remaining nodes perform 3,4,5
#3.if curr & prev is connected:
#4.push(cuur)
#5.call recursively  step 2
#6.if all are visited and path cpontains all nodes, print, return True
#7.

from copy import deepcopy


def getConnectedNodes(node):
    allConnectedNodes =[]
    for toNode in V:
        if E.__contains__(node+toNode) or E.__contains__(toNode+node):
            allConnectedNodes.append(toNode)
    
    return allConnectedNodes


def hamiltonianCycle(visited):
    
    if len(visited) == tot_nodes:
        if E.__contains__(visited[-1]+visited[0]) or E.__contains__(visited[0]+visited[-1]) :
            print('path:',visited)
            return True
        else:
            return False
    
    #if not any visited set curr to start and add it to visisted
    if len(visited) == 0:
        curr = V[0]
        visited.append(curr)
    else:
        curr = visited[-1]

    #Get all connected
    allConneted = getConnectedNodes(curr)
    
    #select only unvisisted from all connected
    unvisited =[]
    for k in allConneted:
        if not(visited.__contains__(k)):
            unvisited.append(k)
    #print('At Node: ',curr ,'to be visisted',unvisited)

    if len(visited) == tot_nodes:
            if E.__contains__(visited[-1]+visited[0]) or E.__contains__(visited[0]+visited[-1]) :
                print('path:',visited)
                return True
            else:
                print('no')
                return False

    for node in unvisited:
        #push the node to the visited stack
        visited.append(node)
    
        #call recursively for that node
        res = hamiltonianCycle(visited)

        #if all connected nodes of this node are visited then pop up this node
        visited.remove(node)

if __name__ == "__main__":
    
    
    V = ['A','B','C','D','E']
    E = ['AB','AD','BD','BC','DC','DE','EC'] 
    G = [V,E]

    visited =[]
    unvisited = deepcopy(V)
    tot_nodes = len(V)
    hamiltonianCycle(visited)

    """
    A----D---E
    |  / |  /
    | /  | /
    B----C
    
    possible hamiltonian cycles are ABCED  and ADECB

    """
